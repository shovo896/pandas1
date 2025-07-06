import pandas as pd
data={'Name':['Rahim','Karim','Shovon'],
       'Age':[25,28,32],
        'City':['New York','London','Paris']
      }
df=pd.DataFrame(data)
second_row=df.iloc[1]
print(second_row)
