'''
# Question 2: Implementing a Shape Hierarchy

class Shape(ABC):
    """
    Design a Python class named `Shape` to represent a geometric shape.

    Theory:
    A shape is a geometric object that has a boundary and can be measured in terms of area and perimeter.

    Operations:
    1. Area: Calculate the area of the shape. (Abstract Method)
    2. Perimeter: Calculate the perimeter of the shape. (Abstract Method)

    Test Cases:
    Test Case 1:
    shape = Rectangle(4, 5)
    assert shape.area() == 20
    assert shape.perimeter() == 18

    Test Case 2:
    # Additional test cases can be added here
    pass


class Rectangle(Shape):
    """
    Design a Python class named `Rectangle` to represent a rectangle.

    Theory:
    A rectangle is a quadrilateral with four right angles.

    Operations:
    1. Area: Calculate the area of the rectangle.
    2. Perimeter: Calculate the perimeter of the rectangle.

    Test Cases:
    Test Case 1:
    rectangle = Rectangle(4, 5)
    assert rectangle.area() == 20
    assert rectangle.perimeter() == 18

    Test Case 2:
    # Additional test cases can be added here
    pass


class Circle(Shape):
    """
    Design a Python class named `Circle` to represent a circle.

    Theory:
    A circle is a simple shape consisting of all points in a plane that are at a given distance from a given center point.

    Operations:
    1. Area: Calculate the area of the circle.
    2. Perimeter: Calculate the perimeter of the circle.

    Test Cases:
    Test Case 1:
    circle = Circle(5)
    assert circle.area() == 78.54
    assert circle.perimeter() == 31.42

    Test Case 2:
    # Additional test cases can be added here
    pass

"""

    
    
'''