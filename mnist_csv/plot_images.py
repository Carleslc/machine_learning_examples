#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Downloaded from train.csv https://www.kaggle.com/c/digit-recognizer/data
CSV = "../large_files/MNIST.csv"

df = pd.read_csv(CSV)
M = df.as_matrix()

def show_example(n):
    label = M[n, 0]
    print(f"Example {n}, digit: {label}")
    im = M[n, 1:] # shape (784,)
    im = im.reshape(28, 28)
    im = 255 - im # negative (digit in black, background in white)
    plt.imshow(im, cmap='gray')
    plt.show()

print(f"Limits 0:{len(M) - 1}")
n_expression = input("start:count\n").split(':')
start, count = max(0, int(n_expression[0])), min(len(M), int(n_expression[1]))
for i in range(start, start + count):
    show_example(i)
