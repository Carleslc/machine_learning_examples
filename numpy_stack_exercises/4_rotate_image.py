#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/learn/v4/t/lecture/7984298

import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt

IMAGE = img.imread("../scipy/image.png")

def rotate_loop(image):
    shape = np.shape(image)
    rows = shape[0]
    cols = shape[1]
    layers = shape[2]
    rotated_image = np.zeros((cols, rows, layers))
    for i in range(rows):
        for j in range(cols):
            for k in range(layers):
                rotated_image[j, rows - 1 - i, k] = image[i, j, k]
    return rotated_image

def rotate(image, k=3):
    return np.rot90(image, k)

rotated_image = rotate(IMAGE)
plt.imshow(rotated_image)
plt.savefig('rot90.png', dpi=300)