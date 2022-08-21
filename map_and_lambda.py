# First Attempt

cube = lambda x: fibonacci**3

def fibonacci(n):
    fib_list = []
    for i in range(int(input())):
        fib_list.append

    for i in fib_list:
        fibbed_list = lambda fib_list[i] + fib_list[i+1]
    print(fibbed_list)

# Solution:

cube = lambda x: pow(x,3)

def fibonacci(n):
    lis = [0,1]
    for i in range(2,n):
        lis.append(lis[i-2] + lis[i-1])
    return(lis[0:n])
