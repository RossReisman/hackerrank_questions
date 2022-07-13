from itertools import combinations_with_replacement

string, num = input(), int(input())

for i in range(len(string)):
    print(*combinations_with_replacement(string, num))


from itertools import combinations_with_replacement

s = input().split()
word, num = sorted(s[0]), int(s[1])

print(*list(map("".join, combinations_with_replacement(word, num))), sep="\n")
