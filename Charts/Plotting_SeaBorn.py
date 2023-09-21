import pandas as pd
import matplotlib.pyplot as plt
import  seaborn as sns

df = pd.read_csv('C:/Users/Adil/Desktop/Python/house-prices.csv')
print(df.head())
print(plt.plot(df['Price']))
print(plt.show())

df['P-S'] = df.Price - df.SqFt
df['100MA'] = df['Bedrooms'].rolling(100).mean()

sns.set_style('darkgrid')

ax = plt.axes(projection='3d')
ax.scatter(df.index,df['P-S'],df['100MA'])
ax.set_xlabel('Index')
ax.set_ylabel('P-S')
ax.set_zlabel('100MA')
print(plt.show())

import numpy as np
z1 = np.linspace(0,10,100)
x1 = np.cos(4*z1)
y1 = np.sin(2*z1)
sns.set_style('darkgrid')
ax = plt.axes(projection = '3d')
ax.plot3D(x1,y1,z1)
print(plt.show())

#Meshgrid
def return_z(x,y):
    return 50-(x**2 + y**2)
sns.set_style('darkgrid')
x1,y1 = np.linspace(-5,5,50),np.linspace(-5,5,50)
x1,y1 = np.meshgrid(x1,y1)
z1 = return_z(x1,y1)
ax = plt.axes(projection = '3d')
ax.plot_surface(x1,y1,z1)
print(plt.show())