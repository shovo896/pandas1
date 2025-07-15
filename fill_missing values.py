import pandas as pd
data = {
    'A':[1,2,3,None],
    'B':[None,2,3,5],
    'C' : [1,2,None,5]





}
df=pd.DataFrame(data)
print(df)

df.fillna(0,inplace=True)
print("\nData after Nan with 0:\n",df)


df.fillna(df.mean(),inplace=True)
print("\nData after Nan with Mean:\n",df)
