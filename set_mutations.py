num_set_a = int(input())
set_a_elements = map(int, input().split())
num_other_sets = int(input())
set_op, *n = input().split()
set_elems = map(int, input().split())

for i in range(num_set_a):
    getattr(set_a_elements, set_op)(*n)

print(set_a_elements)

input()
set_a_elements = set(input().split())
for _ in range(int(input())):
    set_op, *args = input().split()
    getattr(set_a_elements, set_op)(set(input().split()))
print(sum(map(int, set_a_elements)))
