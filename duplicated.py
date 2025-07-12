import pandas as pd
data={
    'Name':['Alice','Rice'],
    'Math':[90,667],
    'History':[75,92]




}
df=pd.DataFrame(data)
print(df.duplicated())
