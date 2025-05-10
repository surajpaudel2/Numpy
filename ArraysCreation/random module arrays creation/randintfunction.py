#Creates and array from the provided range exclusively, where you can also provides the size.
#It by default makes the dtype as int and you cannot change from int8, int32, int64 to others.

import  numpy as np

a1 =  np.random.randint(2, 5699, size=(3, 4, 2)) #Creates an array of shape 3 * 4 * 2, with the random values ranging from 2 to 5699
print(a1)