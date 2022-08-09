# First Attempt

N, X = input().split()
grades = input().split()

zipped = zip(X, grades)

print(zipped)

# Second Attempt:

N, X = input().split()
grades = input().split()

for i in range(int(N)):
    zipped = zip(X, (grades / N))

print(zipped)

# Solution

N, X = map(int, input().split())

sheet = []
for _ in range(x):
    sheet.append(map(float, input().split()))

for i in zip(*sheet):
    print(sum(i) / len(i))
