# Question 1: Class for Complex Numbers
"""
Create a Python class named `ComplexNumber` to represent complex numbers.

Theory:
A complex number is a number that comprises a real part and an imaginary part.
It is typically written in the form a + bi, where 'a' is the real part,
and 'b' is the imaginary part, and 'i' is the imaginary unit (√-1).

Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Comparison (==, !=)
"""
class ComplexNumber:
    def __init__(self,real = 0.0,img = 0.0):
        self.real = real
        self.img = img

    def __str__(self):
        if self.real == 0:
            s = f"Complex Number is: {self.img}i"
        elif self.img >= 0:
            s = f"Complex Number is: ({self.real} + {self.img}i)"
        else:
            s = f"Complex Number is: ({self.real} {self.img}i)"
        return s
    
    def conjugate(self):
        ans = ComplexNumber(self.real, -self.img)
        sign = '-' if ans.img < 0 else '+'
        print(f"Conjugate of Complex Number is: ({ans.real} {sign} {abs(ans.img)}i)")

    # def __add__(c1,c2):        #__add__,__mul__,etc are dunder methods or magic methods
    #     resReal = c1.real + c2.real
    #     resImg = c1.img + c2.img
    #     ans = ComplexNumber(resReal,resImg)
    #     return ans
    #ways to write c1 and c2
    def __add__(self,other):
        resReal = self.real + other.real
        resImg = self.img + other.img
        ans = ComplexNumber(resReal,resImg)
        return ans

    def __sub__(self,other):
        resReal = self.real - other.real
        resImg = self.img - other.img
        ans = ComplexNumber(resReal,resImg)
        return ans

    def __mul__(self,other):
        resReal = (self.real * other.real) + ((-1)*(self.img * other.img))
        resImg = (self.real * other.img) + (other.real * self.img)
        ans = ComplexNumber(resReal,resImg)
        return ans

    def __truediv__(self,other):
        resReal = (self.real * other.real) + (self.img * other.img)
        resImg = (other.real * self.img) - (self.real * other.img)
        deno = (other.real * other.real) + (other.img * other.img) 
        ans = ComplexNumber(resReal/deno,resImg/deno)
        return ans
    
    def magnitude(self):
        return (self.real**2 + self.img**2)**0.5

    # 🔹 Comparison Operators
    def __eq__(self, other):
        return self.real == other.real and self.img == other.img
    
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()
    
    def __le__(self, other):
        return self.magnitude() <= other.magnitude()
    
    def __gt__(self, other):
        return self.magnitude() > other.magnitude()
    
    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()
    
    def __ne__(self, other):
        return not self.__eq__(other)
# c1 and c2 are instance variable which have different values of attribute.
c1 = ComplexNumber(2,1) 
c2 = ComplexNumber(0,1)
print(c1)
print(c2)
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
print(c1 == c2)  
print(c1 != c2)  
print(c1 > c2)  
print(c1 < c2) 

c1.conjugate()
c2.conjugate()