#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import numpy as np

"""
The admission fee at a small fair is $1.50 for children and $4.00 for adults.
On a certain day, 2200 people enter the fair and $5050 is collected.
How many children and adults attended?
"""

"""
Let:

X1 # children
X2 # adults


X1 + X2 = 2200
1.5 * X1 + 4 * X2 = 5050

/ 1    1 \  / X1 \  _  / 2200 \
\ 1.5  4 /  \ X2 /  -  \ 5050 /
"""

A = np.array([[1,1], [1.5, 4]])
b = np.array([2200, 5050])
print(np.linalg.solve(A, b)) # [ 1500.   700.]

"""
Answer:

1500 children
700 adults
"""