#!/usr/bin/python3
"""
Define a class rectangle defined by 1-rectangle.py
"""


class Rectangle:
    """
    define attributes instances
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        intialzie height and width
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        self.__height = value

    def area(self):
        """intialize the area of the rectangle"""
        rec_area = self.__height * self.__width
        return rec_area

    def perimeter(self):
        """Intitialize the perimeter method"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.height + 2 * self.width

    def __str__(self):
        """prints graphical represnation of rectangle"""
        rect = []
        if self.__height == 0 or self.__width == 0:
            return rect
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """return connanical represantation"""
        rep = self.__class__.__name__
        return "{}({}, {})".format(rep, self.__width, self.__height)

    def __del__(self):
        """delete instnace"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
