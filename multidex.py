import pandas as pd


data = {
    "Continent": ["North America", "Europe", "Asia", "North America", "Asia", "Europe", "North America", "Asia", "Europe", "Asia"],
    "Country": ["United States", "Germany", "China", "Canada", "Japan", "France", "Mexico", "India", "United Kingdom", "Nepal"],
    "Population": [331002651, 83783942, 1439323776, 37742154, 126476461, 65273511, 128932753, 1380004385, 67886011, 29136808]
}

# create dataframe from dictionary
df = pd.DataFrame(data)

print(df)

df.sort_values('Continent',inplace=True)
df.set_index(['Continent','Country'],inplace=True)
print(df)
