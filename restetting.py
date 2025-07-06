mport pandas as pd
data={'Name':['Rahim','Karim','Shovon'],
       'Age':[25,28,32],
        'City':['New York','London','Paris']
      }
df=pd.DataFrame(data)
df.rename(index={0:'A',1:'B',2:'C'},inplace=True)
#display dataframe
print('Orginal DataFrame:')
print(df)

df.reset_index(inplace=True)
print('Modified Dataframe ')
print(df)
