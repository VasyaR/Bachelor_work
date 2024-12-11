import torch
import torch.nn.functional as F
from PIL import Image
from .transforms import my_transform, my_transform_inverted
from .model import load_model
from .utils import load_kanji_mapping, load_threshold

def recognize_kanji(image_path, black_background=True, confidence_threshold=-999):
    # Load the model
    model = load_model()

    # Load the kanji mapping
    kanji_mapping = load_kanji_mapping()

    # Load the confidence threshold
    if confidence_threshold == -999:
        confidence_threshold = load_threshold()

    # Load and transform the image
    try:
        image = Image.open(image_path)
    except IOError:
        return "Unsupported file type or file not found"
    
    if black_background:
        image = my_transform(image)
    else:
        image = my_transform_inverted(image)
    image = image.unsqueeze(0)  # Add batch dimension

    # Make the prediction
    with torch.no_grad():
        output = model(image)
        confidence, predicted = F.softmax(output, dim=1).max(dim=1)
    
    # Check confidence threshold
    if confidence.item() < confidence_threshold:
        return "Can't recognize kanji"

    # Convert the predicted index to the corresponding kanji character
    predicted_unicode = kanji_mapping[str(predicted.item())]
    if predicted_unicode.startswith("U+"):
        predicted_kanji = chr(int(predicted_unicode[2:], 16))
    else:
        predicted_kanji = predicted_unicode

    return predicted_kanji