#!/usr/bin/python3
"Defines Square class"


class Square:
    """Initialize a Square object with a given size.

    """
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
