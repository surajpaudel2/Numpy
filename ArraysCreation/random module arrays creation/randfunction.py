import numpy as np

#Creates an array with providing the value from 0 to 1 with uniform distribution.
#takes parameter as d0, d1, d2, ...., dn where these values ranging from d0....dn represents the shape.

a1 = np.random.rand(10 ) #Creates 1D array providing value from 0 to 1 of 10 size.
print(a1)

a1 = np.random.rand(4, 2, 5) # Creates 3D matrix array providing values from 0 to 1 of 4 * 2 * 5 size.
print(a1)