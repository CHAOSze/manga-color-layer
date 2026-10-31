"""Export a square-padded See-through PSD to a registered rectangular AE package.

Requires pillow, numpy and psd-tools[composite]. Input layer order is preserved.
Usage: python export_ae.py input.psd output_dir --width ORIGINAL_WIDTH --height ORIGINAL_HEIGHT
"""
import argparse, json, re
from pathlib import Path
from PIL import Image, ImageDraw
from psd_tools import PSDImage


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('psd',type=Path);p.add_argument('out',type=Path)
    p.add_argument('--width',type=int,required=True);p.add_argument('--height',type=int,required=True)
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True);(a.out/'layers').mkdir(exist_ok=True)
    src=PSDImage.open(a.psd);sw,sh=src.size
    if sw!=sh:raise ValueError('Expected square-padded See-through PSD; inspect geometry before exporting.')
    if min(a.width,a.height)<=0:raise ValueError('Invalid output dimensions')
    ratio=sw/max(a.width,a.height);cw=round(a.width*ratio);ch=round(a.height*ratio)
    x=(sw-cw)//2;y=(sh-ch)//2;crop=(x,y,x+cw,y+ch)
    entries=[];images=[]
    for index,layer in enumerate(src):
        if not layer.is_visible():continue
        im=layer.composite()
        if im is None:continue
        im=im.convert('RGBA');full=Image.new('RGBA',(sw,sh))
        full.alpha_composite(im,(layer.left,layer.top))
        full=full.crop(crop).resize((a.width,a.height),Image.Resampling.LANCZOS)
        bbox=full.getbbox()
        if bbox is None:continue
        tag=layer.name;safe=re.sub(r'[^a-zA-Z0-9_-]+','_',tag).strip('_') or 'part'
        name=f'{len(entries)+1:02d}_{safe}';filename=f'layers/{name}.png';full.save(a.out/filename)
        entries.append(dict(name=name,source_tag=tag,file=filename,bbox=list(bbox),pivot=[(bbox[0]+bbox[2])/2,(bbox[1]+bbox[3])/2]))
        images.append(full)
    if not entries:raise ValueError('No visible nonempty layers')
    merged=Image.new('RGBA',(a.width,a.height));dst=PSDImage.new('RGBA',(a.width,a.height))
    for entry,im in zip(entries,images):
        merged.alpha_composite(im)
        dst.create_pixel_layer(im,name=entry['name'],top=0,left=0)
    dst.save(a.out/'character_layered.psd');merged.save(a.out/'character_composite.png')
    manifest=dict(width=a.width,height=a.height,stack='bottom-to-top',source_square=[sw,sh],source_crop=list(crop),layers=entries)
    (a.out/'layers.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    jsx='''(function(){app.beginUndoGroup("Import semantic layers");try{if(!app.project)app.newProject();var base=new File($.fileName).parent;var data=DATA;var folder=app.project.items.addFolder("Character layers");var c=app.project.items.addComp("Character",data.width,data.height,1,5,24);for(var i=0;i<data.layers.length;i++){var e=data.layers[i];var o=new ImportOptions(new File(base.fsName+"/"+e.file));o.sequence=false;var f=app.project.importFile(o);f.parentFolder=folder;var l=c.layers.add(f);l.name=e.name;l.property("ADBE Transform Group").property("ADBE Anchor Point").setValue(e.pivot);l.property("ADBE Transform Group").property("ADBE Position").setValue(e.pivot);}c.parentFolder=folder;c.openInViewer();}catch(e){alert(e.toString());}finally{app.endUndoGroup();}})();'''
    (a.out/'Import_to_AE.jsx').write_text(jsx.replace('DATA',json.dumps(manifest)),encoding='utf-8')
    tw=320;th=round(tw*a.height/a.width);cols=4;rows=(len(images)+cols-1)//cols
    sheet=Image.new('RGB',(tw*cols,(th+28)*rows),'#858e99');draw=ImageDraw.Draw(sheet)
    for i,(entry,im) in enumerate(zip(entries,images)):
        thumb=im.resize((tw,th),Image.Resampling.LANCZOS);x=i%cols*tw;y=i//cols*(th+28)
        sheet.paste(thumb,(x,y),thumb);draw.text((x+6,y+th+6),entry['name'],fill='white')
    sheet.save(a.out/'layer_overview.png')
    reopened=PSDImage.open(a.out/'character_layered.psd')
    assert reopened.size==(a.width,a.height) and len(reopened)==len(entries)
    report=dict(layer_count=len(entries),canvas=list(reopened.size),psd_reopened=True,ae_executed=False)
    (a.out/'validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report))

if __name__=='__main__':main()
