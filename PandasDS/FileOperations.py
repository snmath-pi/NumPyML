import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = []
for i in range (97, 107):
    character = chr(i)
    labels.append(character)
# print(data)

df2 = pd.DataFrame(data, index = labels)
# print(df2)

df2.to_csv('animal.csv')
df_animal = pd.read_csv('animal.csv')
# print(df_animal.head(3))


df2.to_excel('animall.xlsx', sheet_name='sheet1')
dfs_animal2 = pd.read_excel('animall.xlsx', 'sheet1', index_col=None, na_values = ['NA'])
# print(dfs_animal2)


#series and dataframe line chart




ts = pd.Series(np.random.randn(50), index = pd.date_range('today', periods=50))
ts = ts.cumsum()
print(ts.plot())

