import json

def create_kanji_mapping(dataloader):
    kanji_mapping = {}
    for idx, (images, labels) in enumerate(dataloader):
        for label in labels:
            if label.item() not in kanji_mapping:
                kanji_mapping[label.item()] = idx  # Adjust as necessary
    with open('kanji_recognition/Package/kanji_mapping.json', 'w') as f:
        json.dump(kanji_mapping, f)

def load_kanji_mapping():
    mapping_path = 'kanji_recognition/Package/kanji_mapping.json'
    with open(mapping_path, 'r') as f:
        kanji_mapping = json.load(f)
    return kanji_mapping