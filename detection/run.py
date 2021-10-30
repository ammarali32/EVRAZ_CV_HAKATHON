import sys
import argparse
import os
import torch
from pathlib import Path
from inference import get_detection_solution
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0] 
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  

def main(opt):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    get_detection_solution(path_to_weights =opt.weights,
                               path_to_test_images = opt.data, path_to_dt_ann = opt.output, device = device, img_size = opt.imgsz,sample_path = opt.sub_sample)

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default=ROOT / 'human_detection.pt', help='model path(s)')
    parser.add_argument('--data', type=str, default=ROOT / 'data_task2/test/images', help='images path')
    parser.add_argument('--output', type=str, default=ROOT / 'detection_predictions.json', help='output annotations COCO format')
    parser.add_argument('--sub_sample', type=str, default=ROOT / 'submission_example.json', help='output annotations sample COCO format')
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=2048, help='image size')
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
