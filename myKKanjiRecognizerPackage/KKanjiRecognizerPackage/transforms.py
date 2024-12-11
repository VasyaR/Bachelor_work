from torchvision import transforms
from PIL import Image, ImageOps

def invert_image(image):

    if isinstance(image, Image.Image):
        if image.mode == 'RGBA':
            # Convert RGBA to RGB
            image = image.convert('RGB')
        return ImageOps.invert(image)
    else:
        raise TypeError("Input should be a PIL Image")
    
my_transform = transforms.Compose([

                transforms.Resize(64),  # Resize the smaller edge to 64 while preserving aspect ratio

                transforms.CenterCrop((64, 64)),  # Center crop to 64x64

                transforms.Grayscale(num_output_channels=3),

                transforms.ToTensor(),

                transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])  # Normalize each channel to (-1, 1)  # Normalize to (-1, 1)

            ])

my_transform_inverted = transforms.Compose([

                transforms.Resize(64),  # Resize the smaller edge to 64 while preserving aspect ratio

                transforms.CenterCrop((64, 64)),  # Center crop to 64x64

                transforms.Lambda(invert_image), # invert colors

                transforms.Grayscale(num_output_channels=3),

                transforms.ToTensor(),

                transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])  # Normalize each channel to (-1, 1)  # Normalize to (-1, 1)

            ])