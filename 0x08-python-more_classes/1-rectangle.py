#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """initialize class of rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize rectangle method
        Args:
            height: height of rectangle
            width: width of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width of Rectangle object

        Returns:
            Width vlaue
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the Method of width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Height of Rectangle object

        Returns:
            Height Value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the method of height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
