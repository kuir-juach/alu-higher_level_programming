#!/usr/bin/python3
""" triangle module importing geometry """

:
BaseGeometry =___import___("my_module").BaseGeometry


class Rectangle(BaseGeometry):
    """ rectange class inherit from Base geometry """

    def___init___(self, width, height):
        """ init class """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
