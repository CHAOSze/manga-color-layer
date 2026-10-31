"""Run the reviewed See-through pipeline in independently restartable stages.

Use a compatible CUDA Python environment. This wrapper downloads nothing.
"""
import argparse, gc, os, sys
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True);p.add_argument('--deps',type=Path)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--layer-model',type=Path,required=True);p.add_argument('--depth-model',type=Path,required=True)
    p.add_argument('--resolution',type=int,default=1280);p.add_argument('--depth-resolution',type=int,default=768)
    p.add_argument('--steps',type=int,default=30);p.add_argument('--seed',type=int,default=42)
    p.add_argument('--stage',choices=['check','layers','depth','export','all'],default='all')
    p.add_argument('--no-offload',action='store_true');a=p.parse_args()
    for k in ['repo','deps','input','output','layer_model','depth_model']:
        v=getattr(a,k)
        if v is not None:setattr(a,k,v.resolve())
    a.output.mkdir(parents=True,exist_ok=True)
    os.environ['HF_HOME']=str(a.output/'.hf-cache');os.environ['HF_HUB_OFFLINE']='1';os.environ['TRANSFORMERS_OFFLINE']='1'
    os.environ['OPENBLAS_NUM_THREADS']='8'
    sys.path[:0]=([str(a.deps)] if a.deps else [])+[str(a.repo/'common'),str(a.repo/'annotators')]
    os.chdir(a.repo)
    from utils import inference_utils as iu
    from utils import io_utils
    import numpy as np
    original_default=io_utils.NumpyEncoder.default
    def numpy_default(self,obj):
        if isinstance(obj,np.generic):return obj.item()
        return original_default(self,obj)
    io_utils.NumpyEncoder.default=numpy_default
    from utils.torch_utils import seed_everything
    import torch
    print('CUDA:',torch.__version__,torch.cuda.get_device_name(),flush=True)
    if a.stage=='check':return
    seed_everything(a.seed)
    if a.stage in ['layers','all']:
        iu.apply_layerdiff(str(a.input),str(a.layer_model),save_dir=str(a.output),seed=a.seed,resolution=a.resolution,num_inference_steps=a.steps,group_offload=not a.no_offload)
        iu.layerdiff_pipeline=None;gc.collect();torch.cuda.empty_cache()
    if a.stage in ['depth','all']:
        iu.apply_marigold(str(a.input),str(a.depth_model),save_dir=str(a.output),seed=a.seed,resolution=a.depth_resolution,group_offload=not a.no_offload)
        iu.marigold_pipeline=None;gc.collect();torch.cuda.empty_cache()
    if a.stage in ['export','all']:
        iu.further_extr(str(a.output/a.input.stem),rotate=False,save_to_psd=True,tblr_split=True)
    print('COMPLETE',flush=True)

if __name__=='__main__':main()
