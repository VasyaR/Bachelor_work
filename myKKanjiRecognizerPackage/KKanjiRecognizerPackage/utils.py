import json
import torch

def load_kanji_mapping():
    mapping_path = 'KKanjiRecognizerPackage/PackageData/kanji_mapping.json'
    with open(mapping_path, 'r') as f:
        kanji_mapping = json.load(f)
    return kanji_mapping

def load_threshold():
    threshold_path = 'KKanjiRecognizerPackage/PackageData/threshold.pth'
    threshold = torch.load(threshold_path).item()
    return threshold