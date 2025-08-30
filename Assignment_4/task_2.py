# Task 2: Write and Append Data to a File
 
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

f = open('output.txt','w')
a = input("Enter text to write to file: ")
wr = f.write(a)
print("Data successfully written to output.txt.\n")
f.close()


f = open('output.txt','a')
b = input("Enter additional text to append: ")
wr = f.write("\n")
wr = f.write(b)
print("Data successfully appended.\n")
f.close()

f = open('output.txt','r')
re = f.read()
print("Final content of output.txt: ")
print(re)
f.close()
