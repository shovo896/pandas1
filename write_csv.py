import pandas as pd
data={'Name':['John','Alice','Bob'],
      'Age':[24,25,26],
      'City':['New York','London','Paris']






      }
df=pd.DataFrame(data)
df.to_json('output json',orient='records',indent=4)
