import pandas as pd
data={
    'A' : [1,2,3,3,4,5],
    'B'  :[1,2,3,3,4,5]






}
df=pd.DataFrame(data)
print(df.to_string(index=False))

#detect duplicates

print(df[df.duplicated()].to_string(index=False))

df.drop_duplicates(subset=['A'],keep='first',inplace=True)
print(df.to_string(index=False))
