import pandas as pd
data={
    "Temperature":[22,25,26,32,20],
    "Ice_Cream":[105,120,135,130,125]



}
df=pd.DataFrame(data)
print(df.corr())

correlation=df['Temperature'].corr(df['Ice_Cream'])
print(correlation)
