from collections import Counter

num_shoes = 14
shoe_size = [3, 3, 4, 4, 5, 5, 6, 8, 9, 10, 11, 12, 13, 13]
num_cust = 6
inv_demand = [3, 50, 3, 50, 3, 50, 5, 65, 7, 65, 9, 65]

print(Counter(shoe_size) * inv_demand.values for i in range(1, num_cust))

num_shoes = int(input())
shoes = collections.Counter(map(int(input().split)))
num_cust = int(input())

income = 0

for i in range(num_cust):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1

print(income)
