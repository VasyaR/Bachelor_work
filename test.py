import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np
import pandas as pd
import random
import os

import tqdm

import torchvision
import torchvision.models as models
from torchvision import transforms, datasets
import torch.utils.data as data
import torchvision.datasets
from torch.utils.data.sampler import WeightedRandomSampler
from sklearn.model_selection import train_test_split
from torchvision.models.resnet import conv3x3, _resnet, ResNet18_Weights, BasicBlock, ResNet
import matplotlib.pyplot as plt
import cv2 as cv

random.seed(0)
np.random.seed(0)
torch.manual_seed(0)
torch.cuda.manual_seed(0)
torch.backends.cudnn.deterministic = True
device = 'cpu' # torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

# Paths to data
kkanji_150_path = "/mnt/d/Bachelor_work/data_for_model/kkanji2_150"
kkanji_200_path = "/mnt/d/Bachelor_work/data_for_model/kkanji2_200"
kkanji_300_path = "/mnt/d/Bachelor_work/data_for_model/kkanji2_300"
casia_hwdb_path = "/home/beav3r/Bachelor_work/Bachelor_work/data/CASIA Online and Offline Chinese Handwriting Databases/My_processed_Gnt1.0Test'"
windows_casia_hwdb_train_path = "/mnt/d/Bachelor_work/data_for_model/CASIA_HWDB/train"
windows_casia_hwdb_test_path = "/mnt/d/Bachelor_work/data_for_model/CASIA_HWDB/test"


# For file with filename that has structure symvol: count, sum first 150, sum first 200, sum first 300 counts

# with open("kkanji_classes_distribution_sorted.txt", "r") as f:
#     print("Hi")
#     kkanji_classes_distribution = f.readlines()

#     kkanji_classes_distribution = [line.strip().split(" ") for line in kkanji_classes_distribution]

#     count = 0
#     for i in range(300):
#         count += int(kkanji_classes_distribution[i][1])

#         if i == 149:
#             print("150 classes:", count)
        
#         if i == 199:
#             print("200 classes:", count)
        
#         if i == 299:
#             print("300 classes:", count)

datasets = {0: windows_casia_hwdb_test_path, 1: windows_casia_hwdb_train_path}
for key in datasets:
    print(f"Dataset: {datasets[key]}")
    counter = 0
    for root, dirs, files in os.walk(datasets[key]):
        for dir in dirs:
            counter += 1
        break
    print(f"Number of classes in {datasets[key]}: {counter}")
        
# for root, dirs, files in os.walk(windows_casia_hwdb_test_path):
#     counter = 0
#     for dir in dirs:
#         for root2, dirs2, files2 in os.walk(os.path.join(root, dir)):
#             for file in files2:
#                 print(file)
#                 img = cv.imread(os.path.join(root2, file))
#                 for i in range(img.shape[0]):
#                     for j in range(img.shape[1]):
#                         print(img[i, j])
#                 break
#             break
#         break
#     break

# Before erase
# Test - 9265
# Train - 9600
# After erase
# Test - 6764
# Train - 6764