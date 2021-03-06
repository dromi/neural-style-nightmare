from __future__ import division
import os
import sys

import cv2
import numpy as np

from cmd_format import format_anishathalye, format_jcj

"""
Create tiled images from single image
"""

INPUT = 'local-ns/gogh/base.jpg'
W = 1
H = 1

target_img_size = (500, 500)


def _downscale(image, target_w, target_h):
    im_h, im_w, _ = image.shape
    scale_percent = min(target_h / im_h, target_w / im_w)
    width = int(im_w * scale_percent)
    height = int(im_h * scale_percent)
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)


def tile_image(input_image, width_tiles, height_tiles, dest):
    im1 = cv2.imread(input_image)
    im_height, im_width,_ = im1.shape
    im_v_np = np.tile(im1, (height_tiles, width_tiles, 1))
    resized = _downscale(im_v_np, target_img_size[0], target_img_size[1])
    cv2.imwrite(dest, resized)


def tile_and_train(content_img, tile_img, width_tiles, height_tiles, lr=10, tmp_dest='tmp_tiled.jpg', sim_args='', output_dir=''):
    tile_image(tile_img, width_tiles, height_tiles, tmp_dest)
    output_file_name = content_img.split("/")[-1].split('.')[0] + "-tile-" + str(width_tiles) + "x" + str(height_tiles) + "_lr" + str(lr) + ".jpg"
    # stry = "python impl/neural_style.py --content " + content_img + " --styles " + tmp_dest + " --output " + output_dir + output_file_name + " " + sim_args + " --network impl/imagenet-vgg-verydeep-19.mat --learning-rate " + str(lr)
    stry = format_jcj(content_img, tmp_dest, output=output_dir+output_file_name, sim_args=sim_args)

    print("RUNNING")
    print(stry)
    os.system(stry)
    os.remove(tmp_dest)


if __name__ == '__main__':
    if sys.argv[1] == 'tile':
        tile_image(sys.argv[2], int(sys.argv[4]), int(sys.argv[5]), sys.argv[3])
    else:
        tile_and_train(sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]))