import pandas as pd

#Series
arr1 = [1,2,3,4,5,6]
ser = pd.Series(arr1)
print(ser)

#Element of arr1 change into alphabets
ser1 = pd.Series(arr1,index=['a','b','c','d','e','f'])
print(ser1)
ser2 = pd.Series(arr1,index=['a','b','c','d','e','e'])
print(ser2['e'])