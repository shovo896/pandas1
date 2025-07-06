import pandas as pd
data={'Name':['John','Karim','Rahim','Karime','Kutub','MOSHA'],
      'Age':[25,30,28,33,56,55],
      'city':['New York','Paris','London','Syedney','Tokiyo','Salanga'],
      'Qualifications':['BSC','BBA',',MBA','BSC','SSC','HSC']
      }
df=pd.DataFrame(data)
slice_rows=df.loc[1:3]
print("Sliced Rows:")
print(slice_rows)
print()

slice_columns=df.loc[:,'Name':'Age']
print("Sliced_columns")
print(slice_columns)
