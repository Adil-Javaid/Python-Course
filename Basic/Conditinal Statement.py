import numpy as np
#Where
A = np.arange(10)
print(A)
print("Where: ",np.where(A%2 ==0, 'Even', 'Odd'))

#Select
condlist = [A>5,A<5]
choicelist = [A**2,A**3]
print("Select: ",np.select(condlist,choicelist,default=A))