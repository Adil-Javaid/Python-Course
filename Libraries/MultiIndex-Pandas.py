import pandas as pd
df = pd.read_csv('C:/Users/Adil/Desktop/Python/house-prices.csv')
print(df.head())
print(df.head().set_index(['SqFt','Offers']))
df.set_index(['SqFt','Offers'],inplace=True)
print(df.index)
#Return Vlaue only contain SqFt 1900 &Offers = 2
print(df.loc[1790,2])



