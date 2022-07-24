Attempt 1:

from collections import deque

num_ops = int(input())
methods = input().split()

d = deque()

for elem in methods:
    d.getattr(elem)

print(d)

Attempt 2:

from collections import deque

num_ops = int(input())
methods = input().split()

d = deque()

for elem in range(num_ops):
    getattr(d, methods[elem])

print(d)

Solution:

from collections import deque

d = deque()

for _ in range(int(input())):
    methods, *n = input().split()
    getattr(d, methods) (*n)

print(*d)
