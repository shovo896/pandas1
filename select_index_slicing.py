import pandas as pd

data = {
    'Name': ['John', 'Karim', 'Rahim', 'Karime', 'Kutub', 'MOSHA'],
    'Age': [25, 30, 28, 33, 56, 55],
    'city': ['New York', 'Paris', 'London', 'Syedney', 'Tokiyo', 'Salanga'],
    'Qualifications': ['BSC', 'BBA', ',MBA', 'BSC', 'SSC', 'HSC']
}

df = pd.DataFrame(data)
print(f"Original Dataframe:\n{df}\n")

# Selecting rows 1 to 3 (inclusive) and columns 'Name' and 'Age' using loc
selected_data_loc = df.loc[1:3, ['Name', 'Age']]
print(selected_data_loc.to_string(index=False))
print()

# Selecting rows 1 to 3 (exclusive of 4) and columns 0 ('Name') and 2 ('city') using iloc
selected_data_iloc = df.iloc[1:4, [0, 2]]
print(selected_data_iloc.to_string(index=False))
