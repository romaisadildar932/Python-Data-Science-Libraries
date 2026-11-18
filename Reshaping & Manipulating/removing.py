#delete ->remove element from specific index...np.delete(array,index,axis=None)
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9]) #1d
new_arr = np.delete(arr,1)
print(new_arr)

arr_2d = np.array([[1,2,3,4],[5,6,7,8]])
new_arr_2d= np.delete(arr_2d,0,axis = 0)
print(new_arr_2d)