import  numpy as np

#Construct a 2D matrix filled with 0's everywhere except the diagonals.
#The main arguments are N, M and K, where, N = number of rows we want to construct, M = number of columns and K represents the diagonal meaning in which diagonal you want to put 1.
#If you only provides N then it will create N * N matrix meaning M will also takes the N Value.
#If the provided K is not valid meaning that doesn't fit in the current given matrix size then all the value will be 0's so there is no use of diagonal because all the diagonal will also be filled with 0's.

a1 = np.eye(4) # Matrix of 4 * 4 will be created where all the columns will be filled with 0's except the main diagonal.
print(a1)

#Create a matrix with N*N where -1 diagonal is filled with 1
a1 = np.eye(4, k=-1)
print(a1)

#Create a matrix with N * M where N should be 10 and M should be 8 and provide and provide the k value in such a way that it won't get valid in the current matrix.
a1 = np.eye(10, 8, 100)
print(a1)

#Create N * M matrix with different value for both N and M and provide diagonal in 2.
a1 = np.eye(10, 6, 2)
print(a1)