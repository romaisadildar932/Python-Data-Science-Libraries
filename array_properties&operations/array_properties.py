import numpy as np
arr = np.array([[1,2,3],
                   [4,5,6]])
print(arr)
print(arr.shape) #no. of rows and columns
print(arr.size) #no.of elements
print(arr.ndim) #no. of dimensions
print(arr.dtype) #datatype of array elements
#change the datatype of array element
float_arr = arr.astype(float)
print(float_arr)
print(float_arr.dtype)
