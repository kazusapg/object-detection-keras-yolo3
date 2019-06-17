from PIL import Image
from keras_yolo3.yolo import YOLO
from objects import get_objects_information

if __name__ == '__main__':
    yolo = YOLO()
    image_path = "./picture/sample_picture.jpg"
    objects_info_list = get_objects_information(yolo, image_path)
    yolo.close_session()

    img = Image.open(image_path)
    count = 0
    for object_info in objects_info_list:
        class_name = object_info['predicted_name']
        x = object_info['x']
        y = object_info['y']
        width = object_info['width']
        height = object_info['height']
        cropped_img = img.crop((x, y, x + width, y + height))
        cropped_img.save("./picture/{}{}.jpg".format(class_name, count))
        count = count + 1
