from itertools import combinations

string = input().split()
combo = combinations(string[0], string[1])
print(combo)

from itertools import combinations

s = input().split()
string, number = sorted(s[0]), int(s[1])
for i in range(1, number + 1):
    print(*list(map("".join, combinations(string, i))), sep="\n")

s, n = input().split()
