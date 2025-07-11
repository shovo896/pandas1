import pandas as pd


data={'Data':['2023-08-01','2023-08-01','2023-06-=02','2023-08-01'],
      'Category':['A','B','C','D'],
      'Value':[10,20,30,40]}
df=pd.DataFrame(data)
print("Orginal Dataframe:\n",df)



pivot_df=df.pivot(index='Data',columns='Category',values='Value')
print("Reshaped DataFrame:\n",pivot_df)
