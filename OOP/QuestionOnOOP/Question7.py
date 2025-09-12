'''

# Question: Implementing the Quadrilateral Family

class Quadrilateral:
    """
    Design a Python class named `Quadrilateral` to represent a generic quadrilateral shape.
    The class should include methods to calculate perimeter and area, although the formula for area may not be applicable for all quadrilaterals.
    Quadrilateral is a superclass for other specific types of quadrilaterals.

    Attributes:
    - sides: A list containing the lengths of all four sides of the quadrilateral (list)
    - angles: A list containing the measures of all four angles of the quadrilateral in degrees (list)

    Methods:
    - perimeter(): Calculates and returns the perimeter of the quadrilateral (float)
    - area(): Calculates and returns the area of the quadrilateral (float). Note: The formula for area may not be applicable for all quadrilaterals.

    Test Cases:
    Test Case 1:
    quad1 = Quadrilateral([3, 4, 5, 6], [90, 90, 90, 90])
    assert quad1.perimeter() == 18
    # The sum of all sides = 3 + 4 + 5 + 6 = 18

    Test Case 2:
    quad2 = Quadrilateral([4, 4, 4, 4], [90, 90, 90, 90])
    assert quad2.area() == 16
    # For a square with side length 4, the area is 4 * 4 = 16

    Test Case 3:
    # Additional test cases can be added here


class Rectangle(Quadrilateral):
    """
    Design a Python class named `Rectangle` that inherits from the `Quadrilateral` class.
    The `Rectangle` class represents a rectangle shape.

    Attributes:
    - length: Length of the rectangle (float)
    - width: Width of the rectangle (float)

    Methods:
    - area(): Overrides the area() method from the superclass to calculate and return the area of the rectangle (float)

    Test Cases:
    Test Case 1:
    rect1 = Rectangle(4, 6)
    assert rect1.area() == 24
    # For a rectangle with length 4 and width 6, the area is 4 * 6 = 24

    Test Case 2:
    # Additional test cases can be added here


class Square(Rectangle):
    """
    Design a Python class named `Square` that inherits from the `Rectangle` class.
    The `Square` class represents a square shape.

    Attributes:
    - side_length: Length of the side of the square (float)

    Methods:
    - area(): Overrides the area() method from the superclass to calculate and return the area of the square (float)

    Test Cases:
    Test Case 1:
    square1 = Square(5)
    assert square1.area() == 25
    # For a square with side length 5, the area is 5 * 5 = 25

    Test Case 2:
    # Additional test cases can be added here


class Rhombus(Quadrilateral):
    """
    Design a Python class named `Rhombus` that inherits from the `Quadrilateral` class.
    The `Rhombus` class represents a rhombus shape.

    Attributes:
    - side_length: Length of the side of the rhombus (float)
    - diagonals: Length of the diagonals of the rhombus (list)

    Methods:
    - area(): Overrides the area() method from the superclass to calculate and return the area of the rhombus (float)

    Test Cases:
    Test Case 1:
    rhombus1 = Rhombus(6, [8, 8])
    assert rhombus1.area() == 24
    # For a rhombus with side length 6 and diagonals 8 and 8, the area is (8 * 8) / 2 = 24

    Test Case 2:
    # Additional test cases can be added here


class Parallelogram(Quadrilateral):
    """
    Design a Python class named `Parallelogram` that inherits from the `Quadrilateral` class.
    The `Parallelogram` class represents a parallelogram shape.

    Attributes:
    - base: Length of the base of the parallelogram (float)
    - height: Height of the parallelogram (float)

    Methods:
    - area(): Overrides the area() method from the superclass to calculate and return the area of the parallelogram (float)

    Test Cases:
    Test Case 1:
    parallelogram1 = Parallelogram(5, 8)
    assert parallelogram1.area() == 40
    # For a parallelogram with base 5 and height 8, the area is 5 * 8 = 40

    Test Case 2:
    # Additional test cases can be added here


class Trapezoid(Quadrilateral):
    """
    Design a Python class named `Trapezoid` that inherits from the `Quadrilateral` class.
    The `Trapezoid` class represents a trapezoid shape.

    Attributes:
    - base1: Length of one base of the trapezoid (float)
    - base2: Length of the other base of the trapezoid (float)
    - height: Height of the trapezoid (float)

    Methods:
    - area(): Overrides the area() method from the superclass to calculate and return the area of the trapezoid (float)

    Test Cases:
    Test Case 1:
    trapezoid1 = Trapezoid(3, 5, 4)
    assert trapezoid1.area() == 16
    # For a trapezoid with base1 3, base2 5, and height 4, the area is ((3 + 5) * 4) / 2 = 16

    Test Case 2:
    # Additional test cases can be added here

'''