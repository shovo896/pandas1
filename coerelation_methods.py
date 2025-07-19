import pandas as pd
data={
    "Temperature":[22,25,26,32,20],
    "Ice_Cream":[105,120,135,130,125]



}
df=pd.DataFrame(data)
pearson=df['Temperature'].corr(df["Ice_Cream"])
kendall=df['Temperature'].corr(df["Ice_Cream"],method='kendall')
spearman=df['Temperature'].corr(df["Ice_Cream"],method='spearman')
print(pearson)
print(kendall)
print(spearman)
