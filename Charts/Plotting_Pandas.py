import pandas as pd
import matplotlib.pyplot as mt
df = pd.read_csv('C:/Users/Adil/Desktop/Python/house-prices.csv')
print(df.head())
print(df.columns)
df.plot()
print(mt.show())

#df['Price'].plot()
#print(mt.show())

#df['Price'].plot(legend=True)
#print(mt.show())


#df.plot(x='Bedrooms', y='Price',legend=True)
#print(mt.show())

#df.plot(title='Sample plot', figsize=(10,15))
#print(mt.show())

df['Price'].plot(kind='box',title='box plot')
print(mt.show())

df['Price'].plot(kind='hist',title='Histogram plot')
print(mt.show())
