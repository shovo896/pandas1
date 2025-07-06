import pandas as pd
data={'Name':['John','Karim','Rahim','Karime','Kutub','MOSHA'],
      'Age':[25,30,28,33,56,55],
      'city':['New York','Paris','London','Syedney','Tokiyo','Salanga']}
df=pd.DataFrame(data)
print('Last data Rows:')
print(df.tail(3))
print()

print('Last five Rows:')
print(df.tail())
