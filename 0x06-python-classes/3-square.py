#!/usr/bin/python3
"Define Square class"


class Square:
    "Square class to represent a square"
    def __init__(self, size=0):
        """
                Instantiation with size
        Args:
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return (self.__size * self.__size)
