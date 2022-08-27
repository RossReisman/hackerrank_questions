# First Attempt

import numpy as np

n, m = list(map(int, input().split()))

lis = []
for _ in range(n):
    lis.append(n)
for _ in range(m):
    lis.append(m)

my_array = np.array(lis)
summed = np.sum(my_array, axis=0)
print(np.prod(my_array))

# Solution

import numpy as np

n, m = list(map(int, input().split()))

lis = []
for _ in range(n):
    lis.append(input().split())

my_array = np.array(lis, int)
summed = np.sum(my_array, axis=0)
print(np.prod(summed))
