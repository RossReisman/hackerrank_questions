seta = set(input().split())
num_sets = int(input())
oth_sets = set(input().split())

print(seta.issuperset(oth_sets))
# This is not a issuperset

# Second Attempt:

seta = set(input().split())
num_sets = int(input())
oth_sets = set(input().split())

newset = set()

for i in oth_sets:
    if i in seta:
        newset.add(i)
if newset == seta:
    print("True")
else:
    print("False")
# Failed two of six test cases

# Solution:

A = set(input().split())
print(all([A.issuperset(set(input().split())) for _ in range(int(input()))]))
