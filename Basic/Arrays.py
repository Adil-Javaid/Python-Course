import numpy as np

#Simple Array
array = [1,2,3]
print(array)

#Array with numpy
array1 = np.arange(10)
print(array1)

#Array reshape & 2-D 
array2 = array1.reshape(2,5)
print("2-D ARRAY: \n",array2)

#Array 3-D
array3 = np.arange(64).reshape(4,4,4)
print("3-D ARRAY: \n",array3)

#Array Linespace
array4 = np.linspace(1,5,8).reshape(2,4)
print(array4)

print("\nArray shape: ", array1.shape)
print("\nArray size ", array2.size)
print("\nArray Type: ",array3.dtype)
print("\nArray Type: ",array3.data)
print("\nArray Type: ",array3.itemsize)

array3.reshape(-1)
print("\nArray: ",array3)