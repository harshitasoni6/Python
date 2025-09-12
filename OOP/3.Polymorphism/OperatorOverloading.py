#example 1
# Python program to show use of
# + operator for different purposes.

# print(1 + 2)

# # concatenate two strings
# print("Geeks"+"For") 

# # Product two numbers
# print(3 * 4)

# # Repeat the String
# print("Geeks"*4)

# Example 2
# complexNumber.py we have used magic method.
# When we use an operator on user-defined 
# data types then automatically a special function or 
# magic function associated with that operator is invoked.
# For example, when we use + operator, 
# the magic method __add__ is automatically 
# invoked in which the operation for + operator is defined.

# Example 3
# Python Program illustrate how 
# to overload an binary + operator
# And how it actually works

class A:
    def __init__(self, a):
        self.a = a

    # adding two objects 
    def __add__(self, o):
        return self.a + o.a 
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)
# Actual working when Binary Operator is used.
print(A.__add__(ob1 , ob2)) 
print(A.__add__(ob3,ob4)) 
#And can also be Understand as :
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))