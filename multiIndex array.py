import pandas as pd

# create a dictionary

Continent = ['North America', 'Europe']
Country = ['United States', 'Germany']
Population = [331002651, 83783942]



index_array=[Continent,Country]
multi_index=pd.MultiIndex.from_arrays(index_array,names=['Continent','Country'])
df=pd.DataFrame({'Population':Population},index=multi_index)
print(df)
