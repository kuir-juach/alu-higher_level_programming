#!/usr/bin/python3
""" triangle module importing geometry """


BaseGeometry = _import_("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ rectange class inherit from Base geometry """

    def _init_(self, width, height):
        """ init class """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
