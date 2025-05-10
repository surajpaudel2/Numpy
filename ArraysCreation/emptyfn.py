#Creates and empty array with the provided shape
#NOTE : Empty means, here, it will provides some garbage value because in C it is implementd like that.
import numpy as np

a1 = np.empty(shape=(2, 3, 4))
print(a1)