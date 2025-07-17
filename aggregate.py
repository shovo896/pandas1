import pandas as pd
data={
    'Category':['A','B','C','A','B','C'],
    'Value':[10,15,20,25,30,35]




}
df=pd.DataFrame(data)
total_sum=df['Value'].aggregate('sum')
print(total_sum)
average_value=df['Value'].aggregate('average')
print(average_value)
max_value=df['Value'].aggregate('max')
print(max_value)
