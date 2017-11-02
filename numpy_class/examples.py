#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import numpy as np
import math

# UTILS

def dot_product(a, b):
    """~30 times slower than numpy dot product"""
    dot = 0
    for e1, e2 in zip(a, b):
        dot += e1 * e2
    return dot

## EXAMPLES

print("Python Lists")
a = [1, 2, 3]
b = [4, 5, 6]
print(f"a: { a }\nb: { b }")
print(f"a + b: { a + b }")
print(f"elements a + b: { [e1 + e2 for e1, e2 in zip(a, b)] }")
print(f"2 * a: { 2 * a }")
print(f"elements 2 * a: { [2 * e for e in a] }")
print(f"elements 2 * a (map): { list(map(lambda e: 2 * e, a)) }")
print(f"elements a * b: { [e1 * e2 for e1, e2 in zip(a, b)] }")
print(f"dot product a * b: { dot_product(a, b) }")
print(f"elements sqrt a: { [math.sqrt(e) for e in a] }")
print(f"elements a^b: { [e1 ** e2 for e1, e2 in zip(a, b)] }")
print(f"elements e^a: { [math.e ** e for e in a] }")
print(f"elements log a: { [math.log(e) for e in a] }")

print()

print("NumPy Arrays")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"a: { a }\nb: { b }")
print(f"a + b: { a + b }")
print(f"2 * a: { 2 * a }")
print(f"a * b: { a * b }")
print(f"dot product a * b: { np.sum(a * b) }") # Alternative: (a * b).sum()
print(f"dot product a * b (convenient): { np.dot(a, b) }") # Alternative: a.dot(b)
print(f"norm: { np.linalg.norm(a) }") # Equivalent: np.sqrt( a.dot(a) )
cos = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(f"cosinus angle: { cos }")
print(f"angle: { np.arccos(cos) }") # radians by default
print(f"sqrt a: { np.sqrt(a) }")
print(f"a^b: { a**b }")
print(f"e^a: { np.exp(a) }")
print(f"log a: { np.log(a) }")

print()

print("NumPy Matrices")
m = np.array([[1, 2], [3, 4]])
print(f"m as array of arrays:\n{ m }\n{ type(m) }")
print(f"element at (0,0): { m[0,0] }") # Equivalent: m[0][0]
m = np.matrix([[1, 2], [3, 4]])
print(f"m as matrix:\n{ m }\n{ type(m) }")
print(f"element at (0,0): { m[0,0] }") # Equivalent: m[0][0]
print(f"convert matrix to array:\n{ np.array(m) }")
print(f"transpose matrix:\n{ m.T }")