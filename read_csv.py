import pandas as pd
data={'Name': ['John','Alice','Bob'],
      'Age':[24,45,67],
      'City':['New York','London','Paris']}
df=pd.DataFrame(data)
df.to_csv('Output csv',index=False)
