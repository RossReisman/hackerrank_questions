# First Attempt

import re

S = input()
k = input()

m = re.search(k, S)
print(m.start(), m.end())
# if
# else:
#    print(-1, -1)

# Solution

import re

string = input()
pattern = re.compile(input())
match = pattern.search(string)
if not match:
    print("(-1, -1)")
while match:
    print(f"({match.start()}, {match.end()-1})")
    match = pattern.search(string, match.start() + 1)
