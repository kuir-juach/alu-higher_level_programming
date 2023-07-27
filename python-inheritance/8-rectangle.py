#!/usr/bin/python3
"""
triangle module importing geometry

This module defines a `Rectangle` class that inherits from the `BaseGeometry` class.
"""


BaseGeometry = import("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectange class inherit from Base geometry

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        init(self, width, height): Initialize the rectangle.
        area(self): Calculate the area of the rectangle.
        perimeter(self): Calculate the perimeter of the rectangle.
    """

    def init(self, width, height):
        """
        Init class

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)
