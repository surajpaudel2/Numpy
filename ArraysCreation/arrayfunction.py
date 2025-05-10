import numpy as np
from numpy import dtype

#You can pass list or the tuple to make an array.

a1 = np.array([1, 2, 3,4 ])
a2 = np.array((1, 2, 3, 4, 5))

print(a1, a2)
print(a1.dtype, a2.dtype) # Default is int 64

np.int8(a1) #This will create a new array and it won't be reflected in the original array

a2 = np.array((1, 2, 3, 4,5 ), dtype='int8')

print(a1, a2)
print(a1.dtype, a2.dtype)