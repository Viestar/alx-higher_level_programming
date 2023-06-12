#!/usr/bin/python3
""" MyInt Class Documentation """


class MyInt(int):
    """ MyInt class has been created """

    def __eq__(self, other):
        """ Inverts equal sign to not equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ Inverts not equal sign to Equal"""
        return super().__eq__(other)
