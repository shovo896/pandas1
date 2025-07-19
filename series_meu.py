import pandas as pd
age=pd.Series([29,22,34],name='Age')
sorted_age=age.sort_values()
print(sorted_age)
