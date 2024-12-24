# Steps :
# 1 . Import numpy package
# 2. Create and array depending upon your data types and depending upon your array type [1D, 2D, 3D, 4D....]

import numpy as np # Step 1 of importing numpy package
from numpy import dtype

arr = np.array(([1, 2, 3, 4])) # Step 2 [Creating 1D array]
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) # Step 2 [Creating 2D array]
arr3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]]]) # Step 2 [Creating 3D array]

#----------------------------------------------------------------------------------

#Now you can also give your own data type while creating an array by passing the type of data you want to create by passing the "dtype" argument in the array() function. Below is the example.

arr = np.array([1, 2, 3, 4], dtype=float) # Since, by default provided list makes the array of an integer but due to dtype parameter it will make float data type array.

arr = np.array([1, -1, 2, 3, 4], dtype=bool) # Bool type array will be created

print(arr)

