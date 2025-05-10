# NumPy Random Number Distributions Comparison

# Both rand() and uniform() functions follow the pattern of uniform distribution, but randn() and normal()
# functions follow the normal (Gaussian) distribution. However, they differ in their flexibility.

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

# 4. np.random.normal():
#    - More flexible version of randn()
#    - Generates random numbers from a normal distribution with customizable parameters
#    - Default is standard normal (mean=0, std=1) like randn()
#    - We can provide our desired shape as 'size' parameter
#    - Allows custom mean and standard deviation via parameters
#    - Ideal for modeling real-world phenomena that follow normal distributions


import numpy as np
import matplotlib.pyplot as plt

# Random values from standard normal distribution (mean=0, std=1)
# Shape: 3 rows x 4 columns
standard_normal = np.random.randn(3, 4)
print("randn() with shape (3, 4):")
print(standard_normal)
print()

# Random values from normal distribution with mean=5, std=2
# Shape: 2 rows x 3 columns
custom_normal = np.random.normal(loc=5, scale=2, size=(2, 3))
print("normal() with shape (2, 3), mean=5, std=2:")
print(custom_normal)
print()

# Comparing different distributions
plt.figure(figsize=(15, 5))

# Uniform distribution [0, 1)
plt.subplot(141)
plt.hist(np.random.rand(10000), bins=30, alpha=0.7)
plt.title('rand()\nUniform [0, 1)')
plt.xlim(-5, 10)

# Uniform distribution [-2, 2)
plt.subplot(142)
plt.hist(np.random.uniform(-2, 2, 10000), bins=30, alpha=0.7)
plt.title('uniform(-2, 2)\nCustom Uniform')
plt.xlim(-5, 10)

# Standard normal distribution
plt.subplot(143)
plt.hist(np.random.randn(10000), bins=30, alpha=0.7)
plt.title('randn()\nStandard Normal\n(μ=0, σ=1)')
plt.xlim(-5, 10)

# Custom normal distribution
plt.subplot(144)
plt.hist(np.random.normal(loc=5, scale=2, size=10000), bins=30, alpha=0.7)
plt.title('normal(5, 2)\nCustom Normal\n(μ=5, σ=2)')
plt.xlim(-5, 10)

plt.tight_layout()
plt.show()

# Demonstration of different shapes with normal()
print("normal() with different shapes:")
print("\nShape (3,):")
print(np.random.normal(size=(3,)))
print("\nShape (2, 2):")
print(np.random.normal(size=(2, 2)))
print("\nShape (2, 3, 2):")
print(np.random.normal(size=(2, 3, 2)))