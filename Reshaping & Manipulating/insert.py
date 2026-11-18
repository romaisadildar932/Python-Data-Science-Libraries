#insert ->arr.insert(array,index,value,axis=None)
'''axis = None(insert data in 1d)
axis = 0(insert in row wise)
axis = 1(insert in column wise)'''

import numpy as np
arr = np.array([10,20,30,40,50,60]) #1d
new_arr = np.insert(arr,2,100,axis =0)
print(new_arr)

array = np.array([[1,2,3,4],[5,6,7,8]]) #2d
print(array)
new_array = np.insert(array,1,[50,60],axis=1)
print(new_array)
