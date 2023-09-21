import pandas as pd

df = pd.read_csv('C:/Users/Adil/Desktop/Python/house-prices.csv',index_col=0)
print(df.head())

#Size of dataset
print(df.size)

#Shape of dataset
print(df.shape)

#Colunms of dataset
print(df.columns)

#Create an object from the columns
obj = df[['Price', 'SqFt', 'Bedrooms', 'Bathrooms', 'Offers', 'Brick',
       'Neighborhood']]
print(obj.head())

#Create an object that contain price only
obj_price = df[['Price']]
print(obj_price.head())

#View the shape of object
print(obj_price.shape)

from sklearn.model_selection import train_test_split
x_price, x_SqFt, y_price, y_SqFt = train_test_split(obj, obj_price,random_state=1)
print(x_price.shape)
print(y_price.shape)
print(x_SqFt.shape)
print(y_SqFt.shape)

print(x_price.head())
print(y_price.head())
print(x_SqFt.head())
print(y_SqFt.head())

#Linear Regression Model
from sklearn.linear_model import LinearRegression
linreg= LinearRegression()

#!!!Errors!!!!
#print(linreg.fit(x_price,y_price))
#print(linreg.intercept_)
#print(linreg.coef_)

#y_pred = linreg.predict(x_price)
#print(y_pred)

