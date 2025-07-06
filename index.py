import pandas as pd
data={'Name':['Rahim','Karim','Shovon'],
       'Age':[25,28,32],
        'City':['New York','London','Paris']
      }
df=pd.DataFrame(data)
print(df.index)
print(df.index.values)
