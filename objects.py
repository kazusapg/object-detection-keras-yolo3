import os
from PIL import Image


def get_objects_information(yolo, image_path):
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError
        image = Image.open(image_path)
        return yolo.detect_image(image)
    except FileNotFoundError:
        print("The Image file isn't found. Check the image file path.")
    except IOError:
        print('Image open Error. Try again.')

