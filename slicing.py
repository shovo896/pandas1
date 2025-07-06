import pandas as pd
data={'Name':['John','Karim','Rahim','Karime','Kutub','MOSHA'],
      'Age':[25,30,28,33,56,55],
      'city':['New York','Paris','London','Syedney','Tokiyo','Salanga'],
      'Qualifications':['BSC','BBA',',MBA','BSC','SSC','HSC']
      }
df=pd.DataFrame(data)
slice_rows=df.iloc[1:4]
slice_columns=df.iloc[:,0:2]

# display results
print("Sliced Rows:")
print(slice_rows)
print()
print("Sliced Columns :")
print(slice_columns)
