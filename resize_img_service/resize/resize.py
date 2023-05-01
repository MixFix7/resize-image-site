from PIL import Image
from io import BytesIO

def create_image(img):
    image = Image.open(BytesIO(img))
    height, width = image.size
    return image, height, width



