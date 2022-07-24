eng_num_stu = int(input())
eng_stu_roll = input().split()
fre_num_stu = int(input())
fre_stu_roll = input().split()

eng_set = set(eng_stu_roll)
fre_set = set(fre_stu_roll)

print(len(eng_set.difference(fre_set)))
