#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# Manual parsing and loading

import numpy as np

CSV = "../linear_regression_class/data_2d.csv"

X = []

for line in open(CSV):
    row = line.split(',')
    sample = map(float, row)
    X.append(list(sample))

X = np.array(X)

print(X)
print(np.shape(X))
print(type(X))