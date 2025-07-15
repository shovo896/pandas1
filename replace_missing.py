import pandas as pd
import numpy as np

# create a dataframe with missing values
data1 = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, 5],
    'D': [1, 2, 3, 4, 5]
}
df1 = pd.DataFrame(data1)

# create datframe to fill the missing values with
data2 = {
    'A': [10, 20, 30, 40, 50],
    'B': [10, 20, 30, 40, 50],
    'C': [10, 20, 30, 40, 50],
    'D': [10, 20, 30, 40, 50]
}
df2 = pd.DataFrame(data2)

# replace missing values
df1.fillna(df2, inplace=True)

print(df1)
