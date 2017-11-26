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

# LISTS

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

# ARRAYS

print("NumPy Arrays")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"a: { a }\nb: { b }")
print(f"a + b: { a + b }")
print(f"2 * a: { 2 * a }")
print(f"a * b (element wise): { a * b }")
print(f"a * b (dot product): { np.sum(a * b) }") # Alternative: (a * b).sum()
print(f"a * b (dot product) (convenient): { np.dot(a, b) }") # Alternative: a.dot(b)
print(f"a * b (inner product == dot product): { np.inner(a, b) }")
print(f"a * b (outer product):\n{ np.outer(a, b) }")
print(f"norm: { np.linalg.norm(a) }") # Equivalent: np.sqrt( a.dot(a) )
print(f"euclidian distance between a and b: { np.linalg.norm(a - b) }") # Equivalent: np.sqrt(((v2 - v1)**2).sum())
cos = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(f"cosinus angle: { cos }")
print(f"angle: { np.arccos(cos) }") # radians by default
print(f"sqrt a: { np.sqrt(a) }")
print(f"a^b: { a**b }")
print(f"e^a: { np.exp(a) }")
print(f"log a: { np.log(a) }")
print(f"initialize with zeros: { np.zeros(10) }")
c = np.arange(10)
print(f"initialize with range: { c }")

print()

# MATRICES

print("NumPy Matrices")
c = c.reshape(2, 5)
print(f"reshape array:\n{ c }")
print(f"shape of array or matrix:\n{ np.shape(c) }")
print(f"initalize with zeros:\n{ np.zeros((4, 4)) }") # Also with ones()
print(f"initialize with another value:\n{ np.full((3, 5), 7, dtype=int) }")
print(f"initialize randomly (0~1):\n{ np.random.random((3, 3)) }")
print(f"initialize randomly (gaussian):\n{ np.random.randn(3, 3) }") # Note it is not a tuple
ma = np.array([[1, 2], [3, 4]])
print(f"m as array of arrays:\n{ ma }\n{ type(ma) }")
print(f"element at (0,0): { ma[0,0] }") # Equivalent: ma[0][0]
m = np.matrix([[1, 2], [3, 4]])
print(f"m as matrix:\n{ m }\n{ type(m) }")
print(f"element at (0,0): { m[0,0] }") # Equivalent: m[0][0]
print(f"convert matrix to array:\n{ np.array(m) }")
print(f"convert array to matrix:\n{ np.matrix(ma) }")
print(f"transpose matrix:\n{ m.T }")
print(f"mean:\n{ m.mean() }")
print(f"variance:\n{ m.var() }")
print(f"determinant:\n{ np.linalg.det(m) }")
print(f"inverse:\n{ np.linalg.inv(m) }")
print(f"diagonal:\n{ np.diag(m) }")
print(f"initialize with diagonal:\n{ np.diag([1, 2, 3, 4]) }")
print(f"trace:\n{ np.trace(m) }") # Equivalent: np.diag(m).sum()
print(f"column matrix: { np.matrix([[1], [2], [3], [4]]) }")
print(f"column matrix (reshape): { np.matrix([1, 2, 3, 4].reshape(4, 1)) }")
m[0] = 7
print(f"fill a row with a value:\n{ m }")
m[0] = [1, 2]
print(f"fill a row with values:\n{ m }")
m[:,0] = 5
print(f"fill a column with a value:\n{ m }")
m[:,0] = [[8], [9]]
print(f"fill a column with values:\n{ m }")
a = np.matrix([1, 2, 3])
b = np.matrix([4, 5, 6])
print(f"a: { a }\nb: { b }")
print(f"a * b (element wise): { np.multiply(a, b) }")
print(f"a * b (outer product):\n{ np.outer(a, b) }")
b = b.reshape(3, 1)
print(f"a: { a }\nb: { b }")
print(f"a * b (dot product): { a * b }") # C(a, c) = A(a, b) * B(b, c)

X = np.random.randn(100, 3)
print(f"X gaussian random { np.shape(X) }")
cov = np.cov(X.T) # Note the transpose
print(f"covariance:\n{ cov }")
print(f"covariance:\n{ np.linalg.eigh(cov) }") # Eigenvalue for symmetric and hermitian matrices

# LINEAL SYSTEMS

print("Lineal System")
A = np.array([[1, 2], [3, 4]])
b = np.array([1, 2])
print(f"Solve Ax = b")
print(f"inv(A)Ax = inv(A)b  =>  x = inv(A) * b")
print(f"{ A } x = { b }")
x = np.linalg.solve(A, b) # np.linalg.inv(A).dot(b) --> NOT USE (inefficient and less precise)
print(f"x = { x }")
