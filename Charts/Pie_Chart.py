import matplotlib.pyplot as plt
#matplotlib inline
import pandas as pd
df = pd.read_csv('C:/Users/Adil/Desktop/Python/house-prices.csv')
cause = 'Home', 'Price','Bedrooms','SqFt'
percentile = [25,50,20,5]
plt.figure(figsize=(10,5))
explode = (0.05,0,0,0)
plt.pie(percentile, labels=cause, explode=explode,autopct='%1.1f%%',startangle=70)
plt.axis('equal')
plt.title('Pie Chart')
print(plt.show())