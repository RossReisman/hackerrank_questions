n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N + 1):
    args = input().split()
    s.any(args)
    print(s)


n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    attr, *kw = input().split()
    if kw:
        getattr(s, attr)(*(map(int, *kw)))
    else:
        getattr(s, attr)()
print(sum(s))
