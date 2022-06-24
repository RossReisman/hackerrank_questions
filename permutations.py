from itertools import permutations

s = input().upper().split()
p = permutations(s, 2)
print(p)
