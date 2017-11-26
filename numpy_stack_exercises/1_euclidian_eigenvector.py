#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python/learn/v4/t/lecture/7984298

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[0.3, 0.6, 0.1], [0.5, 0.2, 0.3], [0.4, 0.1, 0.5]])
v = np.random.dirichlet(np.ones(3), size=1)[0] # Random probability distribution of 3 values (sum 1)

print(f'A: {A}')
print(f'Probabilities: {v}')

x = np.linspace(0, 25, 25)
y = np.zeros(25, dtype=object)

def euclidian_distance(v1, v2):
    return np.linalg.norm(v2 - v1)
    #return np.sqrt(((v2 - v1)**2).sum())

for i in range(25):
    v2 = v.dot(A)
    y[i] = euclidian_distance(v, v2)
    v = v2

print(f'Result: {v}')
print(f'y: {y}')

plt.plot(x, y)
plt.show()