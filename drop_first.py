import pandas as pd
data = {'Color': ['Red', 'Green', 'Blue', 'Green', 'Red']}
df = pd.DataFrame(data)
dummies_all = pd.get_dummies(df['Color'])
df_all = pd.concat([df, dummies_all], axis=1)
print("DataFrame with all dummy columns:")
print(df_all)
print("\n")
dummies = pd.get_dummies(df['Color'], drop_first=True)
df = pd.concat([df, dummies], axis=1)
print("DataFrame after dropping 'Blue':")
print(df)
