import pandas as pd



data={'Name':['John','Karim','Rahim','Karime','Kutub','MOSHA'],
      'Age':[25,30,28,33,56,55],
      'city':['New York','Paris','London','Syedney','Tokiyo','Salanga'],
      'Qualifications':['BSC','BBA',',MBA','BSC','SSC','HSC']
      }
df=pd.DataFrame(data)
single_row=df.iloc[2]
row_list=df.iloc[[0,3,4]]
column_list=df.iloc[:,[0,2]]
specific_value =df.iloc[1,0]

print("single Row :")
print(single_row)
print()

print("List of Rows :")
print(row_list)
print()
print("List of Columns :")
print(column_list)
print("Spacific_value:")
print(specific_value)
