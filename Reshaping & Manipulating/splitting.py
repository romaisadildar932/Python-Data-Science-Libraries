'''splitting -> divide the array into subarrays
np.split() ->divide the array into equal parts
np.hsplit() -> horizontally split
np.vsplit() -> vertically split
'''
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(np.split(arr,2))
arr1 = np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])
print(np.hsplit(arr1,2))
print(np.vsplit(arr1,2))

