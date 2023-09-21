import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Adil/Desktop/Python/house-prices.csv')
df.sort_index(inplace=True)
print(df.head())

#Line Plot
print(plt.plot(df['Price']))
print(plt.show())

#Box Plot
print(plt.boxplot(df['Price']))
print(plt.show())

#Histogram
print(plt.hist(df['Price']))
print(plt.show())

#Scatter
plt.xlabel('Price')
plt.ylabel('SqFt')
plt.title('Scatter Plot')
plt.scatter(x=df['Price'], y=df['SqFt'])
print(plt.show())

#Bar Plot
d = {'a':10, 'b':20, 'c':30}
plt.bar(x =d.keys(), height=d.values())
print(plt.show())

#Pie Plot
plt.pie(x = d.values(), labels=d.keys())
print(plt.show())

plt.plot(df['Price'])
plt.figure(figsize=(15,10),dpi =100)
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Line Plotting')
plt.legend()
plt.plot(df['Price'])
print(plt.show())
print(plt.savefig('C:/Users/Adil/Desktop/Python/Price.png'))