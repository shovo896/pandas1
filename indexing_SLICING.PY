import pandas as pd



data={'Name':['John','Karim','Rahim','Karime','Kutub','MOSHA'],
      'Age':[25,30,28,33,56,55],
      'city':['New York','Paris','London','Syedney','Tokiyo','Salanga'],
      'Qualifications':['BSC','BBA',',MBA','BSC','SSC','HSC']
      }
df=pd.DataFrame(data)

name_column=df['Name']
print("Selecting single Column: Name")
print(name_column)
print()

age_city_columns=df[['Age','City']]
print("Selecting multiple columns : Age and city")
print(age_city_columns.to_string(index=False))
print()

#selecting rows using slicing
selected_rows=df[1:4]
print("Slecting rows 1 to 3:")
print(selected_rows.to_string(index=False))
print()
