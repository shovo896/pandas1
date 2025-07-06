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
df.loc[len(df.index)]=['Amy',5.2,'BIT']
print("Modified DataFrame:")
print(df)


df.drop(4,axis=0,inplace=True)
print("MOdified DataFrame:")
print(df)
