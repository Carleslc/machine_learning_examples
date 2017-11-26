#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# LINE CHART

x = np.linspace(0, 10, 100) # Create an axis starting at 0, ending at 10 and with 100 points between
y = np.sin(x) # sinus function for x

plt.plot(x, y)
plt.xlabel("Time (t)")
plt.ylabel("Sin(t)")
plt.title("Sinus function")
plt.show()

# SCATTERPLOT

def plot_correlation(csv, ymax):
    A = pd.read_csv(csv, header=None)
    print(A.head())
    A = A.as_matrix()

    global x, y
    x = A[:,0]
    y = A[:,1]

    x_line = np.linspace(0, 100, 100)
    y_line = (ymax/100)*x_line + 1

    plt.scatter(x, y) # Correlation between columns 0 and 1
    plt.plot(x_line, y_line)
    plt.xlabel("Column 0")
    plt.ylabel("Column 1")
    plt.title("Correlation " + str(csv.split('/')[-1]))
    plt.show()

plot_correlation("../linear_regression_class/data_2d.csv", 100)
plot_correlation("../linear_regression_class/data_1d.csv", 200)

# HISTOGRAM

R = np.random.random(10000)
plt.title("Random distribution")
plt.hist(R, facecolor='green')
plt.show()

N = np.random.randn(10000)
plt.title("Normal distribution")
plt.hist(N, bins=60, facecolor='orange') # bins = number of buckets
plt.show()

plt.hist(x)
plt.title("Histogram data_1d.csv")
plt.show()

y_actual = 2*x + 1
residuals = y - y_actual

plt.hist(residuals)
plt.title("Residuals data_1d.csv")
plt.show()
