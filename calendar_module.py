import calendar

result = input().split()
print(calendar.weekday(result[2], result[1], result[0]))

import calendar

m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
