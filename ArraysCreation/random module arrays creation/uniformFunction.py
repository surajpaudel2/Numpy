#Since rand() function used to provide the value from 0 to 1 with the normal distribution, where there was no choice to provide or say choose from the other numbers. This function provides the flexibility of that. So, in this function you can choose to provide the number from any range to the any range, along with your own desired shape.
#It also follows the normal distribution pattern.

import  numpy as np

a1 = np.random.uniform(low=1, high=100, size=(2, 3, 4))
print(a1)