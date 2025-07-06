mport pandas as pd
data={'Name':['John','Karim','Rahim','Karime','Kutub','MOSHA'],
      'Age':[25,30,28,33,56,55],
      'city':['New York','Paris','London','Syedney','Tokiyo','Salanga'],
      'Qualifications':['BSC','BBA',',MBA','BSC','SSC','HSC']
      }
df=pd.DataFrame(data)
single_row=df.loc[2]
print("single row :")
print(single_row)
print()
row_list=df.loc[[0,2,4]]
print(row_list)
print()
#access a list of columns
column_list=df.list[:,df.loc['Name','Age']]
print("List of columns:")
print(column_list)
print()

# access second row of 'Name' column
specific_value=df.loc[1,'Name']
print("Specific Value :")
print(specific_value)
