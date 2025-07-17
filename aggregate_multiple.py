import pandas as pd
data={
    'Category':['A','B','C','A','B','C'],
    'Value':[10,15,20,25,30,35]




}
df=pd.DataFrame(data)
result=df.groupby('Category')['Value'].agg(['sum','mean','max','min'])
print(result)
