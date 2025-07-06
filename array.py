import pandas as pd
data=[2,4,6,8]
array1=pd.array(data)
print(array1)


float_array=pd.array([1.1,2.2,3.3,4.4],dtype='float')
print(float_array)
print()

string_array=pd.array(['apple','banana','cherry','date'],dtype='str')
print(string_array)
print()

bool_array=pd.array(['True','False','True','False','True'],dtype='bool')
print()


arr=pd.array([12,14,16,17,20])
arr_series=pd.Series(arr)
print(arr_series)
