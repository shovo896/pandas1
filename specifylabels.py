import pandas as pd
a=[1,3,5]
my_series = pd.Series(a,index=["x","y","z"])
print(my_series)
print(my_series["y"])