#!/usr/bin/python3
"""defines a locked class"""


class LockedClass:
    """A class that prevents dynamic instantiation except if `first_name`.

    Atrbs:
    first_name: A firstname string representation."""

    __slots__ = ['first_name']
