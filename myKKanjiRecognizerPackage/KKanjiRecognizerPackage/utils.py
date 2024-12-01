import json

def load_kanji_mapping():
    mapping_path = './PackageData/kanji_mapping.json'
    with open(mapping_path, 'r') as f:
        kanji_mapping = json.load(f)
    return kanji_mapping