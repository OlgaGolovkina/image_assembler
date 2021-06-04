# TODO:
#   - implement an image splitter that split an image into several small parts and mixes them randomly.
#   - update README file.
#   - add linter and mypy, logger
#   - add Docker
#   - add Jenkins

import cv2
import random
import argparse
import numpy as np

"""
This file splits an image with a size of n x n into several small parts and mixes them randomly.
The small parts are then added on a transparent background.

Input parameters:
    -i, --image: path to the image size
    -o, --output: path where the processed image should be saved (path + filename)
    -s, --size: size of the patches (will be squared patches)

Be aware that the image must be the same size in width and height.
"""


class ImageSplitter:

    def __init__(self, params):
        self.params = params
        self.size = int(self.params.size)

    def run(self):
        image = cv2.imread(self.params.image)

        if image.shape[0] != image.shape[1]:
            print('The height and width of the image are different. Please choose another image. '
                  'Please choose an image where the two sizes are the same. ')
            exit(1)

        if image.shape[0] % self.size > 0:
            print('The height and width of the image cannot be divided by the size of the patch. '
                  'Please choose a different patch size that can be used to divide the image.')
            exit(1)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)

        tiles = [image[x:x + self.size, y:y + self.size] for x in range(0, image.shape[0], self.size) for y in
                 range(0, image.shape[1], self.size)]
        first_element = tiles.pop(0)
        random.shuffle(tiles)
        tiles.insert(0, first_element)

        offset = int(self.size / 2)
        row_count = int(image.shape[0] / self.size)

        new_image_size = int(image.shape[0] * 1.5) + offset
        transparent_layer = np.zeros((new_image_size, new_image_size, 4))

        top_point = offset
        left_point = offset
        index_count = 0
        for column in range(0, row_count):
            for row in range(0, row_count):
                transparent_layer[top_point:top_point + self.size, left_point:left_point + self.size, :] = \
                    tiles[index_count]
                left_point = int(left_point + (self.size + offset))
                index_count += 1

            left_point = offset
            top_point = int(top_point + (self.size + offset))

        cv2.imwrite(self.params.output, transparent_layer)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="input image")
    ap.add_argument("-o", "--output", required=True, help="output path of the image")
    ap.add_argument("-s", "--size", required=True, help="size of the cubes")

    args = ap.parse_args()

    splitter = ImageSplitter(args)
    splitter.run()
