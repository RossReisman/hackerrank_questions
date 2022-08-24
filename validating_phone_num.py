# First Attempt

import re

pattern = re.compile(r"[789][0-9]{9}")
fi = pattern.findall(input())

if fi:
    print("YES")
else:
    print("NO")

# Solution

import re

for i in range(int(input())):
    s = input()
    p = re.search(r"^[789]\d{9}$", s)
    if p:
        print("YES")
    else:
        print("NO")
