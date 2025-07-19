import pandas as pd
import matplotlib.pyplot as plt
car=["Caterham","Tesla","Audi","BMW","Ford","Jeep"]
weight=[0.48,1.7,2,2,2.3,3]
data={'car':car,'weight':weight}
df=pd.DataFrame(data)
#plot using pandas
df.plot(x='car',y='weight',kind='bar',color='green')
plt.xlabel('car')
plt.ylabel('weight')
plt.title('car weights(Bar graph)')
plt.show()
