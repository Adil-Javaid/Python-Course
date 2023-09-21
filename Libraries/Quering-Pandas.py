import pandas as pd
s = pd.Series([x for x in range(1,11)])
print("Series: ",s)

print("iloc method use to get value in series: ",s.iloc[0])
print("iat method use to get value in series: ",s.iat[5])
print("Range value in series: ",s[5:9])
print("Where method to get value in series: ",s.where(s%2==0))
print("Put Odd Numbers : ",s.where(s%2==0,'Odd Numbers'))
print("Square Odd Numbers : ",s.where(s%2==0,s**2))
s.where(s%2==0,inplace=True)
print("Drop Odd Numbers : ",s.dropna())
print("Filled Odd Numbers : ",s.fillna("Nothing"))

