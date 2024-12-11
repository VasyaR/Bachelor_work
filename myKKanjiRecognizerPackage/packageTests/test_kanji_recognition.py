from KKanjiRecognizer.recognize_kanji import recognize_kanji
import os

def test_known_black_background():
    # Test a known image with black background
    image_path = "KKanjiRecognizer/PackageData/言_black_background_known.png"
    assert recognize_kanji(image_path) == "言"

def test_known_white_background():
    # Test a known image with white background
    image_path = "KKanjiRecognizer/PackageData/言_white_background_known.png"
    assert recognize_kanji(image_path, black_background=False) == "言"

def test_unknown_black_background():
    # Test an unknown image with black background
    image_path = "KKanjiRecognizer/PackageData/与_black_background_unkown.png"
    assert recognize_kanji(image_path) == "Can't recognize kanji"

def test_unknown_white_background():
    # Test an unknown image with white background
    image_path = "KKanjiRecognizer/PackageData/与_white_background_unkown.png"
    assert recognize_kanji(image_path, black_background=False) == "Can't recognize kanji"

def test_sanity_check():
    # Test the sanity check
    image_path = "KKanjiRecognizer/PackageData/Naruto_sanity_check.png"
    assert recognize_kanji(image_path) == "Can't recognize kanji"

def test_unsupported_file_type():
    # Test an unsupported file type
    image_path = "KKanjiRecognizer/PackageData/unsupported_file_type.txt"
    assert recognize_kanji(image_path) == "Unsupported file type or file not found"