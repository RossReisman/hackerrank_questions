total_num = int(input())
nums = input().split()

print(all(nums))
if nums == nums[::1]:
    print(True)


N = int(input())
integers = input().split()

if all(int(i) >= 0 for i in integers):
    if any(num == num[-1:] for num in integers):
        print("True")
    else:
        print("False")
else:
    print("False")
