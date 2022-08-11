# First Attempt:

T = int(input())
N = [list(input().split()) for _ in range(T)]

for i in range(T):
    if N[1] == ('+' or '-' or '.'):
        print(False)
    elif:

# Solution

import re
for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
