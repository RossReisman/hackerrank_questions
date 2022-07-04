from collections import OrderedDict

N = int(input())
item = input().split()

item_name
item_price

item_dict = OrderedDict()

for item in range(N):
    item_dict.
    print(item_dict)


from collections import OrderedDict

n, item_list = int(input()), OrderedDict()

for _ in range(n):
    item, price = input().rsplit(' ',1)
    item_list.setdefault(item, 0)
    item_list[item] += int(price)
[print(i, v) for i, v in item_list.items()]
