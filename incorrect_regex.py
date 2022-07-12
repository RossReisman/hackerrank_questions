import re

T = int(input())
S = input().split()

for i in range(T):
    r = re.compile(S)
print(r)

import re

T = input()

for i in range(int(T)):
    S = input()
    try:
        re.compile(S)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)
