# First Attempt

import re

S = input()
re.findall(r"[aeiou]+", S)

# Solution

import re

S = input()
pattern = re.compile(r"(?<![AEIOU])([AEIOU]{2,})(?![AEIOU]).", re.I)
fi = pattern.findall(S)
if fi:
    print(*fi, sep="\n")
else:
    print(-1)
