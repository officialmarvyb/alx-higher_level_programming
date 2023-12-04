#!/usr/bin/python3

"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Return obj inherits from a_class.
    """

    return (issubclass(type(obj), a_class) and not (type(obj) is a_class))
