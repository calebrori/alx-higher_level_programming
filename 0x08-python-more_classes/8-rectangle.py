#!/usr/bin/python3
"""This defines a rectangle"""


class Rectangle:
    """A rectangle representation

    Attributes:
        number_of_instances (int): rectangle instances
        print_symbol (any): string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Rectangle width
            height (int): Rectangle height
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Define width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width should be an integer")
        if value < 0:
            raise ValueError("width should be >= 0")
        self.__width = value

    @property
    def height(self):
        """Define height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height should be an integer")
        if value < 0:
            raise ValueError("height should be >= 0")
        self.__height = value

    def area(self):
        """This  returns the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """This returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1: The first Rectangle
            rect_2: The second Rectangle
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 should be instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 should be instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """This returns printable version of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for c in range(self.__height):
            [rect.append(str(self.print_symbol)) for b in range(self.__width)]
            if c != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """This returns string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Prints notification for every deleted rectangle"""
        type(self).number_of_instances -= 1
        print("Gone so soon...")
