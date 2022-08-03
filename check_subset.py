num_test_case = int(input())
num_elem_seta = int(input())
set_a = input().split()
num_elem_setb = int(input())
set_b = input().split()

seta = set(set_a)
setb = set(set_b)

for i in seta:
    if i in setb:
        print("True")
    else:
        print("False")

# Second Attempt:

num_test_case = int(input())
num_elem_seta = int(input())
set_a = input().split()
num_elem_setb = int(input())
set_b = input().split()

seta = set(set_a)
setb = set(set_b)

for i in range(num_test_case):
    print(seta.issubset(setb))

# Solution

for i in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))
