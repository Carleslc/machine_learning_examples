#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/learn/v4/t/lecture/7984298

import numpy as np
import matplotlib.pyplot as plt

def central_limit_theorem(n, examples=1000):
    def random_sum():
        return np.random.random(n).sum()
    y = np.fromfunction(np.vectorize(lambda i,j: random_sum()), (examples, 1))
    plt.hist(y, bins=50)
    plt.show()

for i in range(1, 6):
    n = 10**i
    print(n)
    central_limit_theorem(n)