import cmath

comp_num = input().split()
z, x, y = comp_num[0], comp_num[1], comp_num[2]


print("{:.3f}".format(x, y))

import cmath

r = complex(input().strip())

print(cmath.polar(r)[0])
print(cmath.polar(r)[1])

import cmath

[print(round(i, 3)) for i in cmath.polar(complex(input()))]
