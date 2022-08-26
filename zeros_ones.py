# First Attempt

import numpy as np

n = map(int, input().split())

n_array = np.array(n)

for i in range(n):
    print(np.zeros(n_array))

# Solution

import numpy as np

n = list(map(int, input().split()))
print(np.zeros(n).astype(int))
print(np.ones(n).astype(int))
