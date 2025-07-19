import pandas as pd
data ={
    'Name':['Alice','Bob`'],
    'Age':['28','29'],
    'Score':['85','55']

}
df=pd.DataFrame(data)
print(df)
df1=df.sort_values(by=['Score','Age'])
print(df1)
print(df1.to_string(index=False))
print()

#sortt dataframe in descending order
df2=df.sort_values(by=['Age','Score'], ascending=[True, False])
print(df2)
