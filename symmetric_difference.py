m_size = int(input())
m = map(int, input().split())
n_size = int(input())
n = map(int, input().split()
m_set = set()
n_set = set()
m_set = m
n_set = n
print(m_set.difference(n_set))

m_size, m = (int(input()), input().split())
n_size, n = (int(input()), input().split())

m_set = set(m)
n_set = set(n)

diff1 = m_set.difference(n_set)
diff2 = n_set.difference(m_set)

diff3 = diff1.union(diff2)

print('\n'.join(sorted(diff3, key=int)))
