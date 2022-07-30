group_size = int(input())
room_num_list = list(map(int, input().split()))

for i in room_num_list:
    # count the number of appearances and choose the lowest one
    if room_num_list[i] < group_size:
        print(room_num_list[i])


# Second Attempt:

import pandas as pd

group_size = int(input())
room_num_list = list(map(int, input().split()))

counts = pd.Series(room_num_list).value_counts()
print(counts)

# Couldnt get pandas to import in Hackerrank

# Third Attempt:

group_size = int(input())
room_num_list = list(map(int, input().split()))

for i in room_num_list:
    count1 = room_num_list.count(1)
    count2 = room_num_list.count(2)
    count3 = room_num_list.count(3)
    count4 = room_num_list.count(4)
    count5 = room_num_list.count(5)
    count6 = room_num_list.count(6)
    count7 = room_num_list.count(7)
    count8 = room_num_list.count(8)

    # if room_num_list[i] < group_size:
    print(count1, count2, count3, count4, count5, count6, count7, count8)

# From this we can see that 8 is the only room with 1 member therefore
# it must be the captain's room

# Solution:

from collections import Counter

n = int(input())
rooms = [int(x) for x in input().split()]
cnt = Counter(rooms)

for k, v in cnt.items():
    if v == 1:
        print(k)
        break
