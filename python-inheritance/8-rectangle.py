#!/usr/bin/python3
'''Defines a class Rectangle that inherits from BaseGeometry.'''
baseGeometry = __import__('7base_geometry').BaseGeometry


class Rectangel(BaseGeometry):
    '''Represent a rectangle using BaseGeometry. '''

    def __init__(self, width, height):
        '''Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangel.
            height (int): the height of the new Rectangle.
            '''
            self.integer_validator("width", width)
            self.__width = width
            self.interger_Validator("height",height)
            self.__height = height
