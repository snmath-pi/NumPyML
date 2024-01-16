import numpy as np

#slicing numpy arrays [1d and multid]
np1 = np.array([1, 2, 3, 4, 5, 6])

# if we need a slice [2, 3, 4]

print(np1[1:4])

#numpy slice till the end of the array
# [4, 5, 6..]
print(np1[3:])

#return negative slices starting couting from end backwards

print(np1[-3:-1])

#steps

print(np1[1:5])
print(np1[1:5:2]) 



#steps on entire array

print(np1[::2]) # all the way through the array with steps of 2

#slice a 2-d array
#pull
np2 = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10]])

print(np2[1, 2])

#slice 
print(np2[::, 1:3])
#print(np2[0:2, 1:3])