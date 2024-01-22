import numpy as np

#create a 1-d array and get shape
np1 = np.array([1, 2, 3, 4, 5, 6])
# print(np1)
# print(np1.shape) # just return the lenght of the array for 1-d arrays

#create a 2-d array and get shape

np2 = np.array([[1, 2, 4], [1, 2, 4]])

# print(np2.shape) # basically returns number of rows and columns

#reshape 2-d 
np3 = np1.reshape(3, 2) # make sure it makes sense (3, 4 wtf?)
# print(np3)

#reshape 3-d

npx = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
np4 = npx.reshape(2, 3, 2)
print(np4)
print(np4.shape)



#flatten a numpy array
np5 = np4.reshape(-1)
print(np5)
print(np5.shape)


