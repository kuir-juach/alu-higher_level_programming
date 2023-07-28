#!/usr/bin/python3
""" triangle Rectangle that inherits from Geometry """


BaseGeometry = _import_("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ rectange class tha  inherits from Base geometry """

    def _init_(self, width, height):
        """ init class """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
