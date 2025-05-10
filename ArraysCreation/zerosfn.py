#Function that will generate the array continaing all the values as 0's only.
#Note : You can provide the shape as well like what sort of dimension you want to generate
#Default data type is float.
import numpy as np

a1  = np.zeros(shape=(2, 3, 4), dtype=int) # 3D array containing two 2D matrix with 3 rows for each 2D matrix and 4 columns for each row of 2D matrix will be generated.

print(a1)