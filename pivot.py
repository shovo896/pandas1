import pandas as pd
data={'Name':['John','Karim','Rahim','Karime','Kutub','MOSHA'],
      'Age':[25,30,28,33,56,55],
      'city':['New York','Paris','London','Syedney','Tokiyo','Salanga'],
      'Qualifications':['BSC','BBA',',MBA','BSC','SSC','HSC']
      }
df=pd.DataFrame(data)
print("Orginal Dataframe:\n",df)
pivot_df=df.pivot(index='Age',columns='Name',values='Qualifications')
print("Reshaped DataFrame:\n",pivot_df)
