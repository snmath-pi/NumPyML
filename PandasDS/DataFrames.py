import numpy as np
import pandas as pd


dates = pd.date_range('today', periods = 6) #define time sequence as index
# print(dates)

num_arr = np.random.randn(6, 4)
# print(num_arr)
columns = ['A', 'B', 'C', 'D']


df1 = pd.DataFrame(num_arr, index = dates, columns = columns)
# print(df1)

#create a data fram with dictionary
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

# print(df2.dtypes)

# print(df2.head()) # by default gives 5

df3 = df2.head(6)
# print(df3)

# print(df2.tail(3))


# print(df2.index)
# print(df2.columns)

# print(df2.values)


# print(df2.describe())


# Transpose

# print(df2.T)


# df2.sort_values(by='age')
# print(df2.sort_values(by='age'))


#slicing data frame
# print(df2[:3])


# print(df2.sort_values(by='age')[1:3])



#query data fram by tag
# selecting the columns we wanna work with
# print(df2[['age', 'visits']])


#query rows 2, 3

# print(df2.iloc[1:3])

df3 = df2.copy()
# print(df3)

# print(df3.isnull())


df3.loc['f', 'age'] = 1.5
# print(df3) // changes actual data frame


# print(df3[['age']].mean())
# print(df3['visits'].sum())

# print(df3.sum())




string = pd.Series(['A', 'C', 'D', 'Aaa', 'BaCa', np.nan, 'CBA', 'cow', 'owl'])

# print(string)
# print(string.str.lower())




##### MISSSING VALUES ##################################





df4 = df3.copy()
# print(df4)

# df4.fillna(4)
meanAge = df4['age'].mean()
# print(df4.fillna(meanAge))

df5 = df3.copy()

print(df5.dropna(how = 'any'))









