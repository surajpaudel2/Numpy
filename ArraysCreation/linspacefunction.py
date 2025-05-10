#Function to generate the evenly spaced number from provided start point to ending point inclusively. Hence, if you provide 1 as start and 2 as end then first number will be 1 and end number will be 2 and in the middle there will be all the numbers between 1 and 2.
#By default if you don't provide the "num" parameter then it will generate total of 50 numbers
#It also provides the flexibility of how many numbers we want to generate between those provided start and end
import numpy as np

a1 = np.linspace(1, 2)
print(a1)
print(a1.size)

a1 = np.linspace(1, 2, 39)
print(a1)