#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import numpy as np
import math

print("Python Lists")
a = [1, 2, 3]
b = [4, 5, 6]
print(f"a: {a}\nb: {b}")
print(f"a + b: { a + b }")
print(f"elements a + b: { [e1 + e2 for e1, e2 in zip(a, b)] }")
print(f"2 * a: { 2 * a }")
print(f"elements 2 * a: { [2 * e for e in a] }")
print(f"elements 2 * a (map): { list(map(lambda e: 2 * e, a)) }")
print(f"elements a * b: { [e1 * e2 for e1, e2 in zip(a, b)] }")
print(f"elements sqrt a: { [math.sqrt(e) for e in a] }")
print(f"elements a^b: { [e1 ** e2 for e1, e2 in zip(a, b)] }")
print(f"elements e^a: { [math.e ** e for e in a] }")
print(f"elements log a: { [math.log(e) for e in a] }")
print()
print("NumPy Arrays")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"a: {a}\nb: {b}")
print(f"a + b: { a + b }")
print(f"2 * a: { 2 * a }")
print(f"a * b: { a * b }")
print(f"sqrt a: { np.sqrt(a) }")
print(f"a^b: { a**b }")
print(f"e^a: { np.exp(a) }")
print(f"log a: { np.log(a) }")