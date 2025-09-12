'''
# Question 4: Class for Polynomial
"""
Create a Python class named `Polynomial` to represent polynomials.

Theory:
A polynomial is an expression consisting of variables (or indeterminates) and coefficients,
that involves only the operations of addition, subtraction, multiplication, and non-negative integer exponents.

Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Evaluation: Evaluate the polynomial at a given value
5. Differentiation: Compute the derivative of the polynomial

Test Cases:
Test Case 1:
poly1 = Polynomial([1, 2, 3])
poly2 = Polynomial([3, 4, 5])
assert str(poly1) == "1x^2 + 2x + 3"
assert str(poly2) == "3x^2 + 4x + 5"
assert str(poly1 + poly2) == "4x^2 + 6x + 8"
assert str(poly1 - poly2) == "-2x^2 - 2x - 2"
assert str(poly1 * poly2) == "3x^4 + 10x^3 + 22x^2 + 23x + 15"
assert poly1.evaluate(2) == 17
assert poly2.evaluate(2) == 29

Test Case 2:
poly3 = Polynomial([1, -1])
poly4 = Polynomial([2, -3, 4])
assert str(poly3) == "1x - 1"
assert str(poly4) == "2x^2 - 3x + 4"
"""
'''
class Polynomial:
    pass

