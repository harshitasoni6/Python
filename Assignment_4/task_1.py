# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

try:
    with open('sample.txt','r') as f:
        r_l = f.read()
        print(r_l)
except:
    print("Error:The file sample.txt was not found.")
