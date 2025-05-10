# NumPy Random Number Distributions Comparison

# Both rand() and uniform() functions follow the pattern of uniform distribution, but randn() function follows
# the standard normal distribution (Gaussian distribution with mean 0 and standard deviation 1).

# Key differences between these functions:

# 1. np.random.rand():
#    - Generates random numbers from a uniform distribution over [0, 1)
#    - Each value has equal probability of occurring
#    - We can provide our desired shape as arguments
#    - Output values are always between 0 and 1

# 2. np.random.uniform():
#    - More flexible version of rand()
#    - Generates random numbers from a uniform distribution over [low, high)
#    - Default range is [0, 1) like rand()
#    - We can provide our desired shape as 'size' parameter
#    - Allows custom ranges via low and high parameters

# 3. np.random.randn():
#    - Generates random numbers from a standard normal distribution
#    - Mean = 0, Standard deviation = 1
#    - Values cluster around 0 with approximately 68% within ±1
#    - We can provide our desired shape as arguments
#    - Output values can be positive or negative, typically within ±3

# Examples of providing shapes to these functions:

import numpy as np

# Random values from uniform distribution [0, 1)
# Shape: 3 rows x 4 columns
uniform_2d = np.random.rand(3, 4)
print("rand() with shape (3, 4):")
print(uniform_2d)
print()

# Random values from uniform distribution [-5, 10)
# Shape: 2 rows x 3 columns x 2 depth
uniform_custom = np.random.uniform(-5, 10, size=(2, 3, 2))
print("uniform() with shape (2, 3, 2) and range [-5, 10):")
print(uniform_custom)
print()

# Random values from normal distribution
# Shape: 4 rows x 2 columns
normal_2d = np.random.randn(4, 2)
print("randn() with shape (4, 2):")
print(normal_2d)
print()

# Visualizing the distribution differences
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))

# Uniform distribution [0, 1)
plt.subplot(131)
plt.hist(np.random.rand(10000), bins=30)
plt.title('rand() - Uniform [0, 1)')

# Uniform distribution [-2, 2)
plt.subplot(132)
plt.hist(np.random.uniform(-2, 2, 10000), bins=30)
plt.title('uniform() - Uniform [-2, 2)')

# Normal distribution
plt.subplot(133)
plt.hist(np.random.randn(10000), bins=30)
plt.title('randn() - Standard Normal')

plt.tight_layout()
plt.show()