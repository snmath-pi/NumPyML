import numpy as np

#Copy vs View for numpy

# a copy is a copy of the array but it's not connected to the array
# a view is also a copy of the array but it's connected to the array

np1 = np.array([1, 2, 3, 4, 5])

#view
'''
np2 = np1.view()

print(f'Original np1 {np1}')
print(f'Original np2 {np2}')

np1[0] = 41
print(f'chaned np1 {np1}')
print(f'Original np2 {np2}')

#isme dono mein changes reflect honge agar orignal array mein change hua

np2[1] = 40

print(f'Original np1 {np1}')
print(f'Original np2 {np2}')
#same geos if agar np2 mein changes kare aur np1 mein bhi reflect honge

'''

##Creating a copy

np2 = np1.copy()

print(f'original np1{np1}')

print(f'copied np2 {np2}')

np1[0] = 41
print(f'original np1{np1}')

print(f'copied np2 {np2}') # no changes relfected in the copy



np2[0] = 404004
print(f'original np1{np1}')

print(f'copied np2 {np2}') # similarly copy mein changes karke orignial mein changes reflext nahi hote





 