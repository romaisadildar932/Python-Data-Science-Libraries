#indexing -> access single element,zero-based indexing,also negative(-1,-2) and postive indexing(0,1,2)
'''how to access index
syntax ->array[index] #1d
array[row,column] #2d'''
import numpy as np
arr_1d = np.array([1,2,3,4,5,6])
arr_2d = np.array([[1,2,3,4],[5,6,7,8]])

print(arr_1d[4])
print(arr_1d[-1])
print(arr_2d[1,3])
