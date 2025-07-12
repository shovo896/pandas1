import pandas as pd
data={
    'Name':['Alice','Rice'],
    'Math':[90,667],
    'History':[75,92]




}
df=pd.DataFrame(data)
melted_df=df.melt(df,id_vars='Name',var_name='Subject',value_name='score')
print(melted_df)
