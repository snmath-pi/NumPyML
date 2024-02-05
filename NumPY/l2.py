import numpy as np
#numpy stands for numeric python
#anything in a numpy array have to be of the same data type

# datatype is nd array [n dimensional array]

np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np1)

#basically arrays but more powerful

var = np1.shape # bascially number of elements in our array
print(var)

np2 = np.arange(10) # 10 items in it from [0, 10)
print(np2)

np3 = np.arange(0, 10, 2)
print(np3)




#zeros

np4 = np.zeros(10)
print(np4)


#multidimensional zeros

np5 = np.zeros((2, 10))
print(np5)

#full 

np6 = np.full((10), 6)
print(np6)

np7 = np.full((2, 10), 6)
print(np7)

#convert python list to numpy

my_list = [1, 2, 3, 5, 6]
np8 = np.array(my_list)
print(np8)
print(type(np8))