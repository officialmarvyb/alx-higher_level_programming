#!/usr/bin/python3
"""
  Function that defines
  MyInt that inherits from in
"""


class MyInt(int):
    """Operators == and != is invert."""
    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
