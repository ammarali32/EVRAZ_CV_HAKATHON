import sys
import argparse
import os
import torch
from pathlib import Path
from classification_inference import get_detection
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0] 
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  

def main(opt):
    print(get_detection(image_path = opt.img_path ,weights_path =opt.weights))

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights',  type=str, default=ROOT / 'tf_efficientnet_b1_ns_fold0_best.pth', help='model path(s)')
    parser.add_argument('--img_path', type=str, default=ROOT / 'test.jpg', help='image path')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
