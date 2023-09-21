#Import complete 
import math
A= 16
print(math.sqrt(A))

#Import part
from math import sqrt, sin
print(sqrt(A))
print(sin(A))

#Import Numpy Library
import numpy as np
first_numpy_array = np.array([1,2,3,4])
print(first_numpy_array)

#Array with Zeros
array_with_zeros = np.zeros((3,3))
print(array_with_zeros)

#Array with Ones
array_with_ones = np.ones((3,3))
print(array_with_ones)

#Array with empty
array_with_empty = np.empty((2,3))
print(array_with_empty)

#Array with arange
array_arange = np.arange(12)
print(array_arange)

#Reshape
array_arange.reshape(3,4)
print(array_arange)

#Line space array
linespace = np.linspace(1,6,10)
print(linespace)

#1-D Array
one_D_array = np.arange(15)
print(one_D_array)

#2-D
two_d = one_D_array.reshape(5,3)
print(two_d)

#3-D
three_d = np.arange(27).reshape(3,3,3)
print(three_d)

#Arthimatic Operations
A = np.array([1,2,3])
B = np.array([4,5,6])
print("\nAdd element of array: ",np.add(A,B))
print("\nSubtract element of array: ",np.subtract(A,B))
print("\nMultiplication element of array: ",np.multiply(A,B))
print("\nDivision element of array: ",np.divide(A,B))
print("\nPower element of array: ",np.power(A,B))

