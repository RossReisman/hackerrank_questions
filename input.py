# First Attempt

P = input()
x, k = map(int, input().split())

if eval(P(x) == k):
    print(True)
else:
    print(False)

# Solution

x, k = map(int, input().split())
print(k == eval(input()))
