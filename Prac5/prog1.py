import pandas as pd

d1 = {'Name': ['Rohan', 'Raj', 'Anuj', 'Anil'], 'RollNo': [10, 20, 25, 30], 'Loc' : ['Kurla', 'Kalyan','Mum','Bandra']}
df1 = pd.DataFrame(d1)
print(df1)
print(df1[['Name']])
print(df1[df1.columns[1:2]])
print(df1.loc[1:2, 'Name'])