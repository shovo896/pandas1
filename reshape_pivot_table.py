import pandas as pd


data={
      'Category':['A','B','C','D'],
      'Value':[10,20,30,40]}
df=pd.DataFrame(data)
print("Orginal Dataframe:\n",df)



# using pivot table 

pivot_table_df=df.pivot_table(index='Category',values='Value',aggfunc='mean')
print("Reshaped DataFrame:\n",pivot_table_df)
