#ways of creating list
#creating arrays from python list
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

#with default values ->np.zeros(shape)
arr_zero1 = np.zeros(3)#1d
print(arr_zero1)
arr_zero2 = np.zeros((3,2))#2d
print(arr_zero2)

arr_ones1 = np.ones(3)#1d
print(arr_ones1)
arr_ones2 = np.ones((3,2))#2d
print(arr_ones2)

#with default specific value 
arr_specific1 = np.full(3,5) #1d
print(arr_specific1)
arr_specific2 = np.full((3,5),10) #2d
print(arr_specific2)

#creating seq of numbers in numpy ->np.arange(start,stop,step)
seq = np.arange(5,25,2)
print(seq)

#creating identity matrix
identity = np.eye(4)
print(identity)