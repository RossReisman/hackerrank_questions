err_codes = {v:'ValueError', e:'ZeroDivisionError'}

num_cases = map(int, input())
values = input().split()

for i in values:
    try:
        a/b
    if b == 0:
    except:
        print("Error Code:", e)
    elif b != int:
        print("Error Code:", v)

for test in range(int(input())):
    try:
        a,b = map(int,input().split())
        division_result = a // b
        print(division_result)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
