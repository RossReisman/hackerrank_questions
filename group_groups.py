# First Attempt

import re

S = input().split()

for i in S:
    if re.match([*0 - 9] + 1):
        print(match)
    else:
        print(-1)

# Solution

import re

m = re.search(r"([a-z0-9])\1+", input())
print(m.group(1) if m else -1)
