import pandas as pd
import numpy as np
data={
    'A':[1,2,np.nan,4,5],
    'B':[1,2,3,np.nan,np.nan],
    'C':[1,2,3,4,5]





}
df=pd.DataFrame(data)
df['A'].fillna(value=df['A'].mean(),inplace=True)
#replace missing values with fillna
df['B'].fillna(value=df['B'].median(),inplace=True)

df['C'].fillna(value=df['C'].mode()[0],inplace=True)
print(df)
