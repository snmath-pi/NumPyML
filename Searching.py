import numpy as np

#search
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3])


x = np.where(np1 == 3)

print(x)
print(x[0])

print(np1[x[0]])


#return even items

y = np.where(np1 % 2 == 0)
print(np1[y[0]])