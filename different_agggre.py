import pandas as pd
data={
    'Category':['A','B','C','A','B','C'],
    'Value1':[10,15,20,25,30,35],
    'Value2':[10,15,20,25,30,35]
}
df=pd.DataFrame(data)
agg_funcs={
    'Value1':'sum',
    'Value2':['sum','mean','max','min'],


    }
result=df.groupby('Category').agg(agg_funcs)
print(result)
