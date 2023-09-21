import pandas as pd
import matplotlib.pyplot as plt
import  seaborn as sns

df = pd.read_csv('C:/Users/Adil/Desktop/Python/house-prices.csv')
print(df.head())
print(plt.plot(df['Price']))
print(plt.show())
  
df['P-S'] = df.Price - df.SqFt
df['100MA'] = df['Bedrooms'].rolling(100).mean()

ax = plt.axes(projection='3d')
ax.scatter(df.index,df['P-S'],df['100MA'])
ax.set_xlabel('Index')
ax.set_ylabel('P-S')
ax.set_zlabel('100MA')
print(plt.show())

#Box Plot Sea-born
plt.figure(figsize=(7,7),dpi=100)
plt.title('Box Plot Sea born')
print(sns.boxplot(data = df, x = 'Price'))
print(plt.show())
