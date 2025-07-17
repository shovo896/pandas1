import pandas as pd


data=['red','blue','green','red','blue']
series1= pd.Series(data)
print(series1)

categorical_s=series1.astype('category')
print(categorical_s)
