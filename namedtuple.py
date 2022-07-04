from collections import namedtuple

total_stu = int(input())
col_names = str(input().split())
cols = ({0}, {1}, {2}, {3}).format("marks", "IDs", "name", "class"))
student = namedtuple(name, marks)

avg_marks = sum(student[1]) / len(student[0])

from collections import namedtuple

total_stu = int(input())
fields = input().split()

total = 0
for i in range(total_stu)
    students = namedtuple('student', fields)
    field1, field2, field3, field4 = input().split()
    student = students(field1, field2, field3, field4)
    total += int(student.MARKS)
print('{:.2f}'.format(total/total_stu)

Using Repetition Operator

from collections import namedtuple
n = int(input())
a = input()
total = 0
student = namedtuple('Student', a)
for _ in range(n):
    student = Student(*input().split()
    total += int(student.MARKS)
print('{:.2f}'.format(total/n))
