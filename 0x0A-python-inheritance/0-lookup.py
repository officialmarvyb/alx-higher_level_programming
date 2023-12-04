#!/usr/bin/python3
"""
  Function that defines an object
  attribute lookup.
"""

def lookup(obj):
    """Returns a list of attributes available for an object"""
    return (dir(obj))
