import pandas as pd
df = pd.DataFrame()
print(type(df))

df = pd.read_csv('C:/Users/Adil/Desktop/Python/User.txt')
print(df)
print("Head method to get data: \n",df.head()) #first five rows
print("1st row: \n",df.head(1)) 
print("Tail method to get data: \n",df.tail()) #last five rows
print("Last row: \n",df.tail(1)) 
#Iloc method
print("I loc to get data: \n",df.iloc[0])
print("Print array: \n",df.values)

df = pd.read_csv('C:/Users/Adil/Desktop/Python/User.txt',chunksize=2)
for chunk in df:
    print(chunk)

df = pd.read_csv('C:/Users/Adil/Desktop/Python/controltypes.csv')
df = df[df['Order']>=10]
print(df)
