import numpy as np
arr = np.array([[1,2,3],[4,8,-10]])
print("Minimal value in array is: ",np.amin(arr))
print("Maximal value in array is: ",np.amax(arr))

#horizontal minimal value same for maximum
print("horizontal minimal value: ",np.amin(arr,axis=0))
print("Vartical minimal value: ",np.amin(arr,axis=1))

print("Median: ",np.median(arr))
print("Mean: ",np.mean(arr))
print("Standard deviation: ",np.std(arr))
print("Variance: ",np.var(arr))
print("Percentage: ",np.percentile(arr,100))

#Sin & Cos
deg = np.array([0,30,45,60,90])
print("Sin: ",np.sin(deg*np.pi/180))
print("Cos: ",np.cos(deg*np.pi/180))
print("Tan: ",np.tan(deg*np.pi/180))

#Floor &ceil
arr1 = np.array([0.3,1.3,4.5])
print("Floor: ",np.floor(arr1))
print("Ceil:",np.ceil(arr1))