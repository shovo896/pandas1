import pandas as pd
grades ={ "semester1":3.25 ,"semester2":3.28,"semester3":3.75}
my_series=pd.Series(grades,index=["semester1","semester2"])
print(my_series)
