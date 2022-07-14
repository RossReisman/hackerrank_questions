num_eng_stu = int(input())
eng_stu_roll = input().split()
num_fre_stu = int(input())
fre_stu_roll = input().split()

eng_set = set(eng_stu_roll)
fre_set = set(fre_stu_roll)

diff = eng_set.symmetric_difference(fre_set)

len_diff = len(diff)
print(len_diff)

# diff_count = 0
# for i in diff:
#    diff_count += 1

# print(diff_count)

num_eng_stu = int(input())
eng_stu_roll = input().split()
num_fre_stu = int(input())
fre_stu_roll = input().split()

eng_set = set(eng_stu_roll)
fre_set = set(fre_stu_roll)

not_fre_set = set()
for i in fre_set:
    if i not in eng_set:
        not_fre_set.add(i)

not_eng_set = set()
for i in eng_set:
    if i not in fre_set:
        not_eng_set.add(i)


both_set = not_fre_set | not_eng_set
print(len(both_set))
