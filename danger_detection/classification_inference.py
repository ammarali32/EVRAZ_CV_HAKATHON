# ====================================================
# Library
# ====================================================
import sys
import os
import math
import time
import random
import shutil
from pathlib import Path
import numpy as np
import pandas as pd
import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F
import timm
import warnings

warnings.filterwarnings('ignore')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# ====================================================
# MODEL
# ====================================================
class CustomModel_v2(nn.Module):
    def __init__(self, model_name='tf_efficientnet_b1_ns', pretrained=False):
        super().__init__()
        self.model = timm.create_model(model_name, pretrained=pretrained)
        n_features = self.model.classifier.in_features
        self.model.global_pool = nn.Identity()
        self.model.classifier = nn.Identity()
        self.pooling = nn.AdaptiveAvgPool2d(1)
        self.classifier = nn.Linear(n_features, 2)

    def forward(self, x):
        bs = x.size(0)
        features = self.model(x)
        pooled_features = self.pooling(features).view(bs, -1)
        output = self.classifier(pooled_features)
        return output, features

# ====================================================
# inference
# ====================================================    
def get_detection(image_path, weights_path):
    label = ['Danger', 'Safe']
    #preprocessing
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image,(720,720))
    image =image / 255.0;
    image -=[0.485, 0.456, 0.406]
    image /=[0.229, 0.224, 0.225]
    image = np.transpose(image,(2,0,1))
    image = np.expand_dims(image,0)
    image = torch.from_numpy(image)
    #loading model
    model = CustomModel_v2()
    state = torch.load(weights_path)
    model.load_state_dict(state['model'])
    model.eval()
    #detection
    res, features = model(image.float())
    idx = 1
    if res.softmax(1).detach().numpy()[0][0] > 0.2:
        idx = 0
    return label[idx]

