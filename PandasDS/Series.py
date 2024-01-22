import pandas as pd
import numpy as np

#check pandas version
# print(pd.__version__)

#Series create, manipulate, query, delete

#creating a series from list

arr = [0, 1, 2, 3, 4]
s1 = pd.Series(arr)
# print(s1)


order  = [1, 2, 3, 4, 5]
s2 = pd.Series(arr, index = order)
# print(s2)


arr2 = np.random.randn(5)
# print(arr2)

id = ['a', 'b', 'c', 'd', 'e']

s3 = pd.Series(arr2, index = id)
# print(s3)



#creating a series from a dictionary

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# print(d)
s4 = pd.Series(d)
# print(s3)



#modify the index of the series

s4.index = ['A', 'B', 'C', 'D', 'E']
# print(s4)



#basic slicing

# print(s4[:-2])
# print(s4[:3])

# s5 = s4.append(s3)

s5 = pd.Series([1, 2, 3, 4, 5])
# print(s5)
# s5.drop(0)
# print(s5)

#Series Operations

arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [8, 9, 10, 11, 12]
s5 = pd.Series(arr2)
# print(s5)
s6 = pd.Series(arr1)
# print(s6)

SS = s6.add(s5) # creates a copy and stores it
# print(SS)
SS = s6.multiply(s5)
# print(SS)
# SS = s6.div(s5)
# print(SS)

# print(s6)

print('median', s6.median())
print('max', s6.max())
print('min', s6.min())
print('median of weird', SS.median())

