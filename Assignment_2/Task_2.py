# Task 2: Sum of Integers from 1 to 50 Using a Loop
 
# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.
res = 0
s = 1
e = 51
for i in range(s,e):
    res += i
print(f'The sum of numbers from 1 to 50 is: {res}')