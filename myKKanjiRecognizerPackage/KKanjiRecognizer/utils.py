import json
import torch
import pkg_resources

def load_kanji_mapping():
    mapping_path = pkg_resources.resource_filename('KKanjiRecognizer', 'PackageData/kanji_mapping.json')
    with open(mapping_path, 'r') as f:
        kanji_mapping = json.load(f)
    return kanji_mapping

def load_threshold():
    threshold_path = pkg_resources.resource_filename('KKanjiRecognizer', 'PackageData/threshold.pth')
    threshold = torch.load(threshold_path).item()
    return threshold