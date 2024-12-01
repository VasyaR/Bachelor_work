import torch
import torch.nn as nn
import torch.nn.functional as F

import numpy as np
import pandas as pd
import random
import os
import json

from tqdm import tqdm

import torchvision
import torchvision.models as models
from torchvision import transforms, datasets
import torch.utils.data as data
import torchvision.datasets

from torch.utils.data.sampler import WeightedRandomSampler

from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score, precision_recall_fscore_support
from torchvision.models.resnet import conv3x3, _resnet, ResNet18_Weights

import matplotlib.pyplot as plt
from PIL import ImageOps, Image

random.seed(0)
np.random.seed(0)
torch.manual_seed(0)
torch.cuda.manual_seed(0)
torch.backends.cudnn.deterministic = True

kkanji_150_path = "/mnt/d/Bachelor_work/data_for_model/kkanji2_150"
kkanji_200_path = "/mnt/d/Bachelor_work/data_for_model/kkanji2_200"
kkanji_300_path = "/mnt/d/Bachelor_work/data_for_model/kkanji2_300"

# Dataset initialization

def get_dataloaders(batch_size: int = 16, classamount: int = 150):
    # Define transformations

    my_transform = transforms.Compose([

                transforms.Grayscale(num_output_channels=3),

                transforms.Resize(64),

                transforms.ToTensor(),

                transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])  # Normalize each channel to (-1, 1)  # Normalize to (-1, 1)

            ])



    if classamount == 150:

        # Load dataset 150

        full_dataset = datasets.ImageFolder(root=kkanji_150_path, transform=my_transform)



    elif classamount == 200:

        # Load dataset 200

        full_dataset = datasets.ImageFolder(root=kkanji_200_path, transform=my_transform)



    elif classamount == 300:

        # Load dataset 300

        full_dataset = datasets.ImageFolder(root=kkanji_300_path, transform=my_transform)



    # Split dataset into training and testing sets

    train_indices, test_indices = train_test_split(

        list(range(len(full_dataset))),

        test_size=0.3,

        stratify=[label for _, label in full_dataset.samples]

    )



    train_dataset = data.Subset(full_dataset, train_indices)

    test_dataset = data.Subset(full_dataset, test_indices)



    # Calculate class weights for the training set

    class_counts = [0] * len(full_dataset.classes)

    for idx in train_indices:

        _, label = full_dataset.samples[idx]

        class_counts[label] += 1



    class_weights = [1.0 / count for count in class_counts]
    sample_weights = [class_weights[full_dataset.samples[idx][1]] for idx in train_indices]

    # Create a WeightedRandomSampler for the training set

    sampler = WeightedRandomSampler(weights=sample_weights, num_samples=len(sample_weights), replacement=True)

    # Create DataLoaders

    trainloader = data.DataLoader(train_dataset, batch_size=batch_size, sampler=sampler, num_workers=4)

    testloader = data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=4)



    return trainloader, testloader, full_dataset

# Create kkanji_mapping.json in format {label: class_name}
_, _, data_loader = get_dataloaders(classamount=300)
kanji_mapping = {}
for i in range(len(data_loader.classes)):
    kanji_mapping[i] = data_loader.classes[i]
with open('./myKKanjiRecognizerPackage/KKanjiRecognizerPackage/PackageData/kanji_mapping.json', 'w') as f:
    json.dump(kanji_mapping, f)
