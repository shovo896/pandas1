mport pandas as pd
data={'Name':['John','Karim','Rahim','Karime','Kutub','MOSHA'],
      'Age':[25,30,28,33,56,55],
      'city':['New York','Paris','London','Syedney','Tokiyo','Salanga']}
df=pd.DataFrame(data)

print('First three rows :')
print(df.head(3))
print()

# display first five columns
print('First five rows:')
print(df.head())
