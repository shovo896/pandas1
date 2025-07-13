import pandas  as pd
data1={
    'EmployeeID':['E001','E002','E003','E004','E005'],
    'Name':['John Doe','John Doe','Rahat Khan','Mojila '],
    'Dept ID':['D001','D002','D003','D004','DF005']
    }
employees=pd.DataFrame(data1)
data2={
    'Dept ID': ['D001','D002','D003'],
    'DeptName':['sales','HR','Admin']




}
departments=pd.DataFrame(data2)
df_merge=pd.merge(employees,departments,left_on='DeptID1',right_on='DeptID',sort=True)
print(df_merge)
