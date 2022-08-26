# First Attempt

import numpy as np

my_array = np.array(map(int, input()))
print(np.reshape(my_array, 3, 3))

# Solution

import numpy as np

my_array = np.array(list(map(int, input().split())))
print(np.reshape(my_array, (3, 3)))
