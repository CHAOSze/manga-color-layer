"""Inspect a reference PSD without editing it. Requires psd-tools, Pillow, numpy.

Usage: python audit_psd.py reference.psd report_dir --max-side 1200
Coverage estimates are geometric diagnostics, not measures of artistic quality.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from psd_tools import PSDImage


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('psd', type=Path)
    ap.add_argument('out', type=Path)
    ap.add_argument('--max-side', type=int, default=1200)
    args = ap.parse_args()
    if args.max_side < 64:
        ap.error('--max-side must be at least 64')
    args.out.mkdir(parents=True, exist_ok=True)
    psd = PSDImage.open(args.psd)
    scale = min(1, args.max_side / max(psd.size))
    size = tuple(max(1, round(v * scale)) for v in psd.size)
    rows, masks, cards = [], [], []
    font_path = Path('C:/Windows/Fonts/msyh.ttc')
    font = ImageFont.truetype(str(font_path), 16) if font_path.exists() else ImageFont.load_default()
    for i, layer in enumerate(psd.descendants()):
        row = dict(index=i, name=layer.name, kind=layer.kind,
                   visible=layer.is_visible(), opacity=layer.opacity,
                   bbox=list(layer.bbox), group=layer.is_group(),
                   parent=layer.parent.name, blend_mode=str(layer.blend_mode))
        rows.append(row)
        if layer.is_group():
            continue
        raster = layer.composite(force=True)
        if raster is None:
            row['empty'] = True
            continue
        raster = raster.convert('RGBA')
        row['empty'] = raster.getbbox() is None
        thumb = raster.copy()
        thumb.thumbnail((300, 260))
        card = Image.new('RGB', (340, 320), '#888888')
        card.paste(thumb, ((340-thumb.width)//2, 40), thumb)
        ImageDraw.Draw(card).text((8, 8), f'{i}: {layer.name}', font=font, fill='white')
        cards.append(card)
        # Maintain document coordinates; never independently center parts for overlap analysis.
        tile = raster.resize((max(1, round(raster.width*scale)), max(1, round(raster.height*scale))))
        canvas = Image.new('RGBA', size)
        canvas.alpha_composite(tile, (round(layer.left*scale), round(layer.top*scale)))
        masks.append((row, np.asarray(canvas.getchannel('A')) > 127))
    flat_normal = all(not r['group'] and r['opacity'] == 255 and r['blend_mode'] == 'BlendMode.NORMAL' for r in rows)
    cover = np.zeros(size[::-1], dtype=bool)
    if flat_normal:
        for row, mask in reversed(masks):
            area = int(mask.sum())
            row['estimated_hidden_fraction'] = float((mask & cover).sum()/area) if area else None
            if row['visible']:
                cover |= mask
    composite = psd.composite()
    if composite is not None:
        composite.thumbnail(size)
        composite.save(args.out/'composite.png')
    for start in range(0, len(cards), 12):
        batch = cards[start:start+12]
        sheet = Image.new('RGB', (1360, 320*((len(batch)+3)//4)), '#333333')
        for j, card in enumerate(batch):
            sheet.paste(card, ((j%4)*340, (j//4)*320))
        sheet.save(args.out/f'parts_{start//12+1:02}.jpg')
    report = dict(canvas=list(psd.size), layers=rows, coverage_computed=flat_normal,
                  note='Approximate alpha>127 overlap at reduced scale for flat, opaque, normal stacks only. Hidden coverage does not prove correct inpainting. Groups, effects and unusual blending require visual review.')
    (args.out/'audit.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Inspected {len(rows)} entries; output: {args.out}')


if __name__ == '__main__':
    main()
