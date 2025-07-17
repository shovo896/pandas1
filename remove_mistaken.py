import pandas as pd
data = {
    'Name': ['John', 'Michael', 'Tom', 'Alex', 'Ryan'],
    'Age': [8, 9, 7, 80, 100],
    'Gender': ['M', 'M', 'M', 'M', 'M'],
    'Standard': [3, 4, 12, 3, 5]
}
df = pd.DataFrame(data)
# replace values based on conditions
for i in df.index:
    if df.loc[i,'Standard'] > 3 :
        df.drop(i,inplace=True)
print(df)
