#Expanding single elements
import numpy as np
arr = np.array([10,20,30,40])
res = arr * 2
print(res)

#Mathematical Dimensions
matrix = np.array([[1,2,3],[4,5,6]]) #2d
vector = np.array([10,20,30]) #1d
res = matrix + vector
print(res)

#Incompatible shapes
arr1 = np.array([[1,2,3],[4,5,6]]) #2d
arr2 = np.array([10,20]) #1d
result = arr1 + arr2
print(result)#error