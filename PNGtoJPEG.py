import sys
import os
from PIL import Image


class ImageConverted():
    def __init__(self):
        self.image_dir = sys.argv[1]
        self.new_image_dir = sys.argv[2]
        self.images_list = os.listdir(self.image_dir)

    def check_dir(self):
        if not os.path.exists(self.new_image_dir):
            os.makedirs(self.new_image_dir)
        return self.convert_images()

    def convert_images(self):
        for image in self.images_list:
            img = Image.open(self.image_dir + image)
            rgb_img = img.convert('RGB')
            rgb_img.save(f"{self.new_image_dir}{os.path.splitext(image)[0]+'.jpg'}")


if __name__ == '__main__':
    convert = ImageConverted()
    convert.check_dir()