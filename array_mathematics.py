# First Attempt

import numpy as np

n, m = list(map(int, input().split()))
a = np.array(input().split(), int)
b = np.array(input().split(), int)

print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.floor_divide(a, b))
print(np.mod(a, b))
print(np.power(a, b))

# Solution

import numpy as np

n, m = list(map(int, input().split()))

a = []
b = []

for _ in range(n):
    a.append(input().split())
A = np.array(a, int)
for _ in range(n):
    b.append(input().split())
B = np.array(b, int)

print(
    np.add(A, B),
    np.subtract(A, B),
    np.multiply(A, B),
    np.floor_divide(A, B),
    np.mod(A, B),
    np.power(A, B),
    sep="\n",
)
