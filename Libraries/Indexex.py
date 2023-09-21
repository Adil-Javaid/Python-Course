import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("One-D Array: ",arr1)
print("Two-D Array: ",arr2)
print("Three-D Array: ",arr3)

#Indexex
#--1-D ARRAY
print("One-D Index#1: ",arr1[0])
print("One-D Index#2: ",arr1[1])
print("One-D Index#3: ",arr1[2])

#2-D Array
print("Two-D Index#0,0: ",arr2[0,0])
print("Two-D Index#0,1: ",arr2[0,1])
print("Two-D Index#1,2: ",arr2[1,2])

#3-D Array
print("Three-D Index#0,0,2: ",arr3[0,0,2])
print("Three-D Index#0,1,2: ",arr3[0,1,2])
print("Three-D Index#1,0,2: ",arr3[1,0,2])
print("Three-D Index#1,1,2: ",arr3[1,1,2])
