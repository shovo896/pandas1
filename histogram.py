import pandas as pd
import matplotlib.pyplot as plt
weight=[0.48,1.7,2,3]
data={"Weight":weight}
df=pd.DataFrame(data)
#histogram using pandas
df['Weight'].plot(kind='hist',bins=10,edgecolor='black',color='red')
plt.show()
