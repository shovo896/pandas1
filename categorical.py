import pandas as pd
from pandas.io.stata import categorical_conversion_warning

data=['red','blue','green','red','blue']
categorical_data = pd.Series(data)
print(categorical_data)
