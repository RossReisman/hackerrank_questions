num_stamps = int(input())
stamps = input().split()

stamps_set = set(stamps)

for i in stamps:
    stamps_set.add(i)
print(len(stamps_set))

num_stamps = int(input())
stamps_set = set()

for i in range(num_stamps):
    stamps = input()
    stamps_set.add(stamps)
print(len(stamps_set))
