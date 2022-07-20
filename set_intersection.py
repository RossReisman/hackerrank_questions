num_eng_stu = int(input())
eng_stu_roll = input().split()
num_fre_stu = int(input())
fre_stu_roll = input().split()

eng_stu_set = set(eng_stu_roll)
fre_stu_set = set(fre_stu_roll)

print(len(eng_stu_set.intersection(fre_stu_set)))
