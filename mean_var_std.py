# First Attempt

import numpy as np

n, m = list(map(int, input().split()))

lis = []
for _ in range(n):
    lis.append(input().split())

my_array = np.array(lis, int)
print(np.mean(my_array, axis=1), np.var(my_array, axis=0), np.std(my_array), sep="\n")

# Solution

import numpy as np

n, m = list(map(int, input().split()))

lis = []
for _ in range(n):
    lis.append(input().split())

my_array = np.array(lis, int)
print(
    np.mean(my_array, axis=1),
    np.var(my_array, axis=0),
    round(np.std(my_array), 11),
    sep="\n",
)
