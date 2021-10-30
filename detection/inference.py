import os
import json
import torch
import cv2
from tqdm import tqdm


from detection.yolov5.utils.general import non_max_suppression, scale_coords, xyxy2xywh
from detection.yolov5.utils.augmentations import letterbox
from detection.yolov5.models.experimental import attempt_load

image_dic = dict()

def preprocess(path_to_img, img_size, device):
    print(path_to_img)
    orig_img = cv2.imread(path_to_img)
    print(orig_img.shape)
    orig_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)
    img = letterbox(orig_img, img_size, auto=False)[0]
    img = img.transpose(2, 0, 1)
    img_tensor = torch.from_numpy(img).float().to(device)
    img_tensor /= 255
    img_tensor = img_tensor.unsqueeze(0)
    return img_tensor, list(orig_img.shape), list(img_tensor.shape)


def postprocess(
    out,
    tensor_shape,
    orig_shape,
    path_to_img,
    conf_thres=0.6,
    iou_thres=0.6,
    counter = 1,
):
    out = non_max_suppression(out, conf_thres, iou_thres)
    img_predict = []
    idx = path_to_img.split('/')[-1:][0]
    print(idx)
    idx = image_dic[idx]
    for pred in out:
        pred[:, :4] = scale_coords(tensor_shape[2:], pred[:, :4], orig_shape).round()
        box = xyxy2xywh(pred[:, :4])  # xywh
        box[:, :2] -= box[:, 2:] / 2
        for p, b in zip(pred.tolist(), box.tolist()):
            img_predict.append(
                {
                    "id" : counter,
                    "image_id": int(idx),
                    "category_id": 1,
                    "segmentation":[],
                    "area":b[2] * b[3],
                    "bbox": [round(x, 3) for x in b],
                    "iscrowd": 0,
                    "attributes":{"occluded":False}
                }
            )
            counter += 1
    return img_predict, counter


def get_img_predict(model, path_to_img, device, img_size, counter = 1):
    img_tensor, orig_shape, tensor_shape = preprocess(path_to_img, img_size, device)
    with torch.no_grad():
        out, _ = model(img_tensor, augment=False)
    img_predict, counter = postprocess(out, tensor_shape, orig_shape, path_to_img,counter = counter)
    return img_predict, counter


def get_detection_solution(
    path_to_weights =['yolov5/runs/train/exp2048/weights/best.pt',] , path_to_test_images = "data_task2/test/images", path_to_dt_ann = 'detection_predictions.json', device = None, img_size = 2048,
    sample_path = 'data_task2/submission_example.json'
):
    detect_model = attempt_load(path_to_weights, map_location=device)
    detect_model.eval()
    result = []
    ann = json.load(open(sample_path))
    for i in range(len(ann['images'])):
        image_dic[ann['images'][i]['file_name']] = ann['images'][i]['id']
    counter = 1
    for file in tqdm(ann['images']):
        file_name = file['file_name']
        img_predict, counter = get_img_predict(
            detect_model, os.path.join(path_to_test_images, file_name), device, img_size, counter
        )
        result.extend(img_predict)
    ann['annotations'] = result
    with open(path_to_dt_ann, "w") as f:
        json.dump(ann, f)
