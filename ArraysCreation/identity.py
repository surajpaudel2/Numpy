#Provides pure identity matrix i.e. 2D matrix filled with all 0's except the main diagonal. So, in this matrix there is no need to provide the M value infact it doesn't take M argument as well.
#Provide N value and matirx will automatically be created as N * N with main diagonal as 1's
import numpy as np

a1 = np.identity(3, dtype='int8')
print(a1)