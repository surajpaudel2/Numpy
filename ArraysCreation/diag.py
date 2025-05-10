import numpy as np

# How diag function works?

# 1. It can only be used with 1D and 2D arrays.
# 2. It takes v and k parameters where:
#    - v is the input array (1D or 2D)
#    - k is an integer specifying which diagonal (default k=0 for main diagonal)

# 3. For 1D array input:
#    - Creates a new square 2D array with zeros everywhere
#    - Places the 1D array elements along the diagonal specified by k
#    - If k=0 (default): Places elements on the main diagonal
#    - If k>0: Places elements on the kth diagonal above the main diagonal
#    - If k<0: Places elements on the |k|th diagonal below the main diagonal
#    - The output shape will be (n+abs(k), n+abs(k)) where n is the length of input

# 4. For 2D array input:
#    - Extracts the diagonal elements from the 2D array
#    - Returns them as a new 1D array
#    - If k=0 (default): Extracts the main diagonal
#    - If k>0: Extracts the kth diagonal above the main diagonal
#    - If k<0: Extracts the |k|th diagonal below the main diagonal
#    - If k value exceeds matrix bounds, returns empty array
#    - For a matrix of shape (m,n), valid k values range from -m+1 to n-1

# 5. Mathematical significance:
#    - For 1D→2D: Creates a diagonal matrix (important in linear algebra)
#    - For 2D→1D: Extracts eigenvalues (when applied to square matrices)

# 6. Common use cases:
#    - Creating identity matrices: np.diag(np.ones(n))
#    - Extracting main diagonal: np.diag(matrix)
#    - Creating scaling matrices: np.diag([x, y, z])
#    - Checking for dominant diagonals: np.diag(matrix).sum() > threshold

# 7. Limitations:
#    - Cannot directly work with arrays of dimension > 2
#    - Use np.diagonal() instead for higher dimensions
#    - Returns a copy, not a view (changes to output won't affect input)




#PROVIDING 1D ARRAY AS THE PARAMETER IN diag FUNCTION.

# a1 = np.array([1, 4, 3, 2])
# my_List = [1, 4, 3, 2]
# my_Tup = [1, 4, 3, 2]
#
# # a2 = np.diag(a1, k=8)
# # print(a2)
#
# # a2 = np.diag(my_List, k = 8)
# # print(a2)
#
# a2 = np.diag(my_Tup, k = 8)
# print(a2)

# a1 = [1, 2, 3, 4]
# a2 = np.diag(a1)
# print(a2)

#PROVIDING 2D ARRAY AS THE PARAMETER IN diag FUNCTION

# a1 = np.random.randint(2, 10, size=(4, 5))
# print(a1)
#
# # a2 = np.diag(a1, k = 2)
# # print(a2)
#
# a2 =  np.diag(a1, k=10)
# print(a2)


#Working with 3D array in Diag function Will give an error.

# a1 = np.random.randint(2, 10, size=(2, 3, 4))
# print(a1)
#
# a2 = np.diag(a1, k = 1)
#
# print(a2)
