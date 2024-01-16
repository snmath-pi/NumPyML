import numpy as np

#sorting this is numerical
np1 = np.array([6, 5, 7, 1, 2, 4])

print(np1)

print(np.sort(np1))


#alphbetical

np2 = np.array(["john", "tina", "eren", "a", "skasham"])

print(np2)
print(np.sort(np2))


# can also sort booleans
np3 = np.array([True, False, True, False])
print(np3)
print(np.sort(np3))


#sort returns a copy we are not changing the original at all
print(np1)
print(np.sort(np1))
print(np1)


np4 = np.array([[6, 7, 4], [12, 11, 130]])

print(np4)
print(np.sort(np4)) # sorts inside each individual rows

