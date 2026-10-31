"""Motion-conditioned post-processing of a reviewed semantic PSD.

This is a local extension, not a trained model. A user-reviewed plan explicitly
defines degrees of freedom and contiguous source bundles. No inferred anatomical
class is automatically treated as an independently moving object.
"""
from pathlib import Path
import argparse
import json
import numpy as np
from PIL import Image
from psd_tools import PSDImage

MODES = {'fixed', 'rigid', 'bend', 'bridge', 'breath'}


def validate_plan(plan, count):
    cursor = 0
    ids = set()
    for part in plan['parts']:
        if part['id'] in ids:
            raise ValueError('Duplicate part id: ' + part['id'])
        ids.add(part['id'])
        sources = part['sources']
        if not sources or sources != list(range(cursor, cursor + len(sources))):
            raise ValueError('Bundles must partition the original stack in order; crossing an intervening occluder changes drawing order')
        cursor += len(sources)
        if part['mode'] not in MODES:
            raise ValueError('Unknown motion mode')
        if not part.get('reason'):
            raise ValueError('A part needs a motion reason, not just an anatomical name')
        if part['mode'] in {'bend', 'bridge', 'breath'} and not part.get('pins'):
            raise ValueError('A deformable part needs a root/attachment plan')
    if cursor != count:
        raise ValueError('The plan must account for every source layer exactly once')


def canvas_layer(layer, size):
    im = layer.composite().convert('RGBA')
    full = Image.new('RGBA', size)
    full.alpha_composite(im, (layer.left, layer.top))
    return full


def premultiplied(im):
    ar = np.asarray(im).astype(np.float32) / 255
    ar[:, :, :3] *= ar[:, :, 3:4]
    return ar


def compile_motion_parts(src, plan, output):
    src, output = Path(src), Path(output)
    if isinstance(plan, (str, Path)):
        plan = json.loads(Path(plan).read_text(encoding='utf-8'))
    psd = PSDImage.open(src)
    # Unsupported blending is rejected instead of silently flattened incorrectly.
    for layer in psd:
        if layer.is_group() or not layer.is_visible() or layer.opacity != 255 or str(layer.blend_mode) != 'BlendMode.NORMAL':
            raise ValueError('This adapter accepts reviewed flat, visible, normal, full-opacity pixel layers only')
    validate_plan(plan, len(psd))
    if plan.get('canvas') and tuple(plan['canvas']) != psd.size:
        raise ValueError('Plan coordinates do not match PSD canvas; unpad/scale the plan explicitly')
    output.mkdir(parents=True, exist_ok=True)
    (output / 'layers').mkdir(exist_ok=True)
    target = PSDImage.new('RGBA', psd.size)
    before, after = Image.new('RGBA', psd.size), Image.new('RGBA', psd.size)
    sources = [canvas_layer(layer, psd.size) for layer in psd]
    for im in sources:
        before.alpha_composite(im)
    entries = []
    bundled = []
    for part in plan['parts']:
        im = Image.new('RGBA', psd.size)
        for idx in part['sources']:
            im.alpha_composite(sources[idx])
        bundled.append(im)
    routed_regions = []
    id_to_index = {part['id']:i for i,part in enumerate(plan['parts'])}
    for index,part in enumerate(plan['parts']):
        region = part.get('rigid_root_region')
        if not region:
            continue
        dest = id_to_index[region['target']]
        other = plan['parts'][dest]
        if other['mode'] not in {'fixed','rigid'} or other.get('parent') != part.get('parent'):
            raise ValueError('A rigid root must retain its parent transform and go to a rigid/fixed part')
        ar = np.array(bundled[index]);piece = np.zeros_like(ar)
        x0,y0,x1,y1 = region['rect']
        piece[y0:y1,x0:x1] = ar[y0:y1,x0:x1]
        ar[y0:y1,x0:x1] = 0
        bundled[index] = Image.fromarray(ar)
        bundled[dest].alpha_composite(Image.fromarray(piece))
        routed_regions.append(dict(part=part['id'],target=other['id'],pixels=int((piece[:,:,3]>0).sum())))
    # Strengthen a reviewed root only where higher layers fully hide it.
    # This uses existing low-alpha color, never dilates arbitrary silhouettes.
    root_repairs = []
    cover = np.zeros((psd.height, psd.width), np.float32)
    for part, im in reversed(list(zip(plan['parts'], bundled))):
        ar = np.array(im)
        rect = part.get('hidden_root_rect')
        if rect:
            region = np.zeros(cover.shape, bool)
            x0,y0,x1,y1 = rect
            region[y0:y1,x0:x1] = True
            take = region & (ar[:,:,3] > 8) & (ar[:,:,3] < 255) & (cover > .999)
            ar[take,3] = 255
            im.paste(Image.fromarray(ar))
            root_repairs.append(dict(part=part['id'], strengthened_pixels=int(take.sum())))
        alpha = ar[:,:,3].astype(np.float32)/255
        cover = alpha + cover*(1-alpha)
    for i, part in enumerate(plan['parts']):
        image = bundled[i]
        if image.getbbox() is None:
            raise ValueError('Empty motion part: ' + part['id'])
        name = f'{i+1:02} {part["name"]}'
        layer = target.create_pixel_layer(image, name=part['id'])
        layer.name = name
        filename = f'layers/{i+1:02}_{part["id"]}.png'
        image.save(output / filename)
        after.alpha_composite(image)
        entries.append(dict(part, index=i, file=filename, bbox=list(image.getbbox())))
    delta = np.abs(premultiplied(before) - premultiplied(after))
    # Integer alpha grouping may introduce at most small rounding error.
    if delta.mean() > .001 or delta.max() > 3/255:
        raise ValueError('Rest composition changed beyond grouping tolerance')
    target.save(output / 'character_motion.psd')
    check = PSDImage.open(output / 'character_motion.psd')
    assert len(check) == len(entries) and check.size == psd.size
    after.save(output / 'character_composite.png')
    manifest = dict(width=psd.width, height=psd.height, stack='bottom-to-top',
                    intent=plan['intent'], controls=plan.get('controls', {}), layers=entries)
    (output / 'layers.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    report = dict(input_layers=len(psd), motion_parts=len(entries), psd_reopened=True,
                  rest_premultiplied_mean_error=float(delta.mean()),
                  rest_premultiplied_max_error=float(delta.max()), hidden_root_repairs=root_repairs,rigid_root_routing=routed_regions,
                  note='Grouping preserves rest artwork; mesh quality, occlusion completion and motion need separate tests. No model was trained.')
    (output / 'compile_validation.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    return manifest


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--src', required=True)
    p.add_argument('--plan', required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    result = compile_motion_parts(args.src, args.plan, args.output)
    print('Compiled', len(result['layers']), 'motion parts')


if __name__ == '__main__':
    main()
