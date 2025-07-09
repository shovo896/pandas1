import pandas as pd
data={'Name':['John','Karim','Rahim','Karime','Kutub','MOSHA'],
      'Age':[25,30,28,33,56,55],
      'city':['New York','Paris','London','Syedney','Tokiyo','Salanga'],
      'Qualifications':['BSC','BBA',',MBA','BSC','SSC','HSC']
      }
df=pd.DataFrame(data)


#df for duplicate entries
print(df.duplicated())

#check for duplicate entries in columns and  Age
print(df.duplicated(subset=['Name','Age']))

df.drop_duplicates(inplace=True)
print(df)


#remove duplicates and keep last entries
df.drop_duplicates(keep='last',inplace=True)
print(df)
