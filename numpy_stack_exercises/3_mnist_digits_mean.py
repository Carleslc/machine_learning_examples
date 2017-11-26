#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/learn/v4/t/lecture/7984298

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

CSV = "../large_files/MNIST.csv"

df = pd.read_csv(CSV)

def mean_digit(n):
    examples = df[df.label == n].drop('label', axis=1)
    sum_examples = examples.sum()
    mean = sum_examples / len(examples)
    mean = mean.values.reshape(28, 28)
    mean = 255 - mean # negative (digit in black, background in white)
    plt.imshow(mean, cmap='gray')
    plt.show()

for i in range(10):
    print(i)
    mean_digit(i)