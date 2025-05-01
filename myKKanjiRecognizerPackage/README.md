This package is created for recognizing kanji from images. 
The model that is used for recognizing is Preact-Resnet-18.
Model can destinguish 300 classes with most sample from KKanji https://github.com/rois-codh/kmnist.
The model was trained on 64x64 grayscale images with white kanji on black backgound.
You are able to use function recognize_kanji() with black_background=False in case you have the opposite situation.
Also, in case you want to experiment more, you can change model_confidence from 0 to 1, but the initial value
is set with value, that showed best performance during our experiments.
Visual representation should be also available on Hugging face, name is the same as the package name. 
https://huggingface.co/spaces/Beav3r/KKanjiRecognizer