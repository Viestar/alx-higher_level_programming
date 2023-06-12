#!/usr/bin/python3
"""MyList class Documentation"""


class MyList(list):
    """Derived class "MyList" from list """

    def print_sorted(self):
        """ Returns a sorted list """

        print(sorted(self))
