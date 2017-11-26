#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/learn/v4/t/lecture/7984298

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def xor(x, y):
    return (x > 0) ^ (y > 0)

def custom(x, y):
    return x + y < 0.25 and x + y > -0.25

def random_range(min, max, n):
    return (max - min) * np.random.random(n) + min

N = 3000
x = np.linspace(-1, 1, N)
y = random_range(-1, 1, N)
cmap = colors.ListedColormap(['darkblue', 'darkred'])
xor_colors = [xor(i, j) for i, j in zip(x, y)]

plt.scatter(x, y, c=xor_colors, cmap=cmap, alpha=0.8)
plt.show()