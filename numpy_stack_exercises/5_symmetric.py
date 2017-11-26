#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/learn/v4/t/lecture/7984298

import numpy as np

def is_symmetric(matrix):
    return (matrix == matrix.T).all()

def is_symmetric_float(matrix):
    return np.allclose(matrix, matrix.T)

m = np.arange(9).reshape(3,3) + 1
print(m)
print(is_symmetric(m))

m = np.array([[1,2,3],[2,4,5],[3,5,6]])
print(m)
print(is_symmetric(m))