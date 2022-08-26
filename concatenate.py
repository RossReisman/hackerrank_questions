# First Attempt

import numpy as np

n, m, p = list(map(int, input().split()))
n_lines = list(map(int, input().split()))
m_lines = list(map(int, input().split()))

n_array = np.array(n_lines)
m_array = np.array(m_lines)

for _ in range(p):
    print(np.concatenate((n_array, m_array), axis=0))

# Solution

import numpy as np

N, M, P = map(int, input().split(" "))

arr1 = np.array([input().split(" ") for i in range(N)], dtype=int)
arr2 = np.array([input().split(" ") for i in range(M)], dtype=int)

print(np.concatenate((arr1, arr2), axis=0))
