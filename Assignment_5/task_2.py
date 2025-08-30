# Task 2: Demonstrate List Slicing 
# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

li = [i for i in range(1,11)]
first_five = li[:5]
print("Original list: ",li)
print("Extracted first five elements: ",first_five)
first_five.reverse()
print("Reversed extracted elements: ",first_five)

