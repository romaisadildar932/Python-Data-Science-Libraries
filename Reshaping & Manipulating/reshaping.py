#reshaping -> changing dimensions without modify data,only reshape when dimensions match...syntax ->array.reshape(rows,columns)
import numpy as np
arr = np.array([10,20,30,40,50,60])
print(arr)
print(arr.reshape(2,3))
