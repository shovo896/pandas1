import pandas as pd
data={'Name':['John','Karim','Rahim','Karime','Kutub','MOSHA'],
      'Age':[25,30,28,33,56,55],
      'city':['New York','Paris','London','Syedney','Tokiyo','Salanga'],
      'Qualifications':['BSC','BBA',',MBA','BSC','SSC','HSC']
      }
df=pd.DataFrame(data)
print("Orginal Dataframe:")
print(df)
print()

df.rename(index={0:7},inplace=True)
df.rename(mapper={1:10,2:100},axis=0,inplace=True)
print("Modified Dataframe:")
print(df)
