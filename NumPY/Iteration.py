import numpy as np
#1d

np1 = np.array([1, 2, 3, 4, 5, 66])

# for x in np1:
#     print(x)

np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# for x in np2:
#     #print the rows 
#     print(x)
    
# #getting inside

# for x in np2:
#     for y in x:
#         print(y)

#3d array

np3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(np3)

# for x in np3:
#     # print(x)
#     for y in x:
#         # print(y)
#         for z in y:
#             print(z)
            
            
#Another way np.nditer()

for x in np.nditer(np3):
    print(x)
