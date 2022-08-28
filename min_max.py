# First Attempt

import numpy as np

n, m = list(map(int, input().split()))

lis = []
for _ in range(n):
    lis.append(input().split())

my_array = np.array(lis, int)
min_array = np.min(my_array, axis=1)
print(max(min_array))

# Solution

import numpy as np

n, m = list(map(int, input().split()))

lis = []
for _ in range(n):
    lis.append(input().split())

my_array = np.array(lis, int)
min_array = np.min(my_array, axis=1)
print(max(min_array))

# Got it right!
