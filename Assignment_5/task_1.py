# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

student_name = {
    "Arya" : 90,
    "Harshita" : 100,
    "Sikha" : 80,
    "Apoorv" : 100,
    "Samay" : 70
    }
s = input("Enter the student's name: ")
if s in student_name:
    print(f"{s}'s marks: {student_name[s]}")
else:
    print("Student not found.")