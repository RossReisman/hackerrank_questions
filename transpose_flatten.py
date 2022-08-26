# First Attempt

import numpy as np

my_array = np.array(list(map(int, input().split())))
col_elems = list(map(int, input().split()))

print(np.transpose(my_array))
print(my_array.flatten())

# Solution

import numpy as np

n, m = list(map(int, input().split()))
arr = []

for i in range(n):
    arr.append(input().split())

new_arr = np.array(arr, int)
print(np.transpose(new_arr), new_arr.flatten(), sep="\n")
