# First Attempt

import email.utils

for i in range(int(input())):
    pattern = re.compile(r"[/w][-._]@[/w].[/w]{1-3}")
    print(email.utils.formataddr(input().split()), sep="\n")

# Solution

import re

n = int(input())

for i in range(n):
    input_data = input().split()
    unformatted_input_data_1 = input_data[1]
    input_data[1] = input_data[1][1 : len(input_data[1]) - 1]
    pattern = "^[a-zA-Z][a-zA-Z0-9-_.]*[@][a-zA-Z]+[.][a-zA-Z]{1,3}$"
    result = re.match(pattern, input_data[1])
    if result != None:
        print(" ".join([input_data[0], unformatted_input_data_1]))
