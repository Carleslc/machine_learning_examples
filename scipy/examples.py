#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from scipy.stats import norm
from scipy.stats import multivariate_normal as mvn

# Probability Density Function (PDF)
norm.pdf(0) # probability of 0 with gaussian distribution
norm.pdf(0, loc=5, scale=10)

# Probability of 10 values
r = np.random.randn(10)
norm.pdf(r)

# joint probability p(x1..xn) = x1 * .. * xn
# log of joint probability
norm.logpdf(r)

# Cummulative Distribution Function (Integral from -Inf to Inf of PDF)
norm.cdf(r)
norm.logcdf(r)

std = 10 # standard deviation
mean = 5
r = std*np.random.randn(10000) + mean
h = plt.hist(r, bins=50)
print(h)
plt.show()

# Spherical Gaussian (uncorrelated multi-dimensional with same variance)
r = np.random.randn(10000, 2)
plt.scatter(r[:,0], r[:,1])
plt.show()

# Elliptical Gaussian (uncorrelated multi-dimensional with different variance)
std = 5
mean = 2
r[:,1] = std*r[:,1] + mean
plt.scatter(r[:,0], r[:,1])
plt.axis('equal')
plt.show()

# Covariance Matrix
# Variance 1 in first dimension and 3 for the second dimension
# Covariance of 0.8 between each dimension
cov_matrix = np.array([[1, 0.8], [0.8, 3]])

# Mean 0 for first dimension and 2 for the second dimension
mu = np.array([0, 2])
r = mvn.rvs(mean=mu, cov=cov_matrix, size=1000) # random following the specified details
plt.scatter(r[:,0], r[:,1])
plt.show()

r = np.random.multivariate_normal(mean=mu, cov=cov_matrix, size=1000)
plt.scatter(r[:,0], r[:,1])
plt.axis('equal')
plt.show()


# OTHER USEFUL FUNCTIONS

# Load a MATLAB (.mat) file
# scipy.io.loadmat

# Load a WAV file
# scipy.io.wavfile

# Fourier Transformation
x = np.linspace(0, 100, 10000) # Some Frequencies
y = np.sin(x) + np.sin(3*x) + np.sin(5*x) # Multiple components
plt.plot(y)
plt.show()

print("Original Frequencies from FFT (peaks x ~ 16, 48, 80)")
def getFreq(x):
    return 2*np.pi*x/100
print(f"F1: {getFreq(16)}, F2: {getFreq(48)}, F3: {getFreq(80)}")

Y = np.fft.fft(y)
plt.plot(np.abs(Y))
plt.show()

# Signal Processing (Convolution, Filters...)
# scipy.signal
plt.figure()
image = img.imread('image.png')
plt.imshow(image)
plt.title('Original image')
plt.show()

f_image = image[:,:,0]
plt.imshow(f_image)
plt.gray()
plt.title('Filtered image')
plt.show()