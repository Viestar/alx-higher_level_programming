#!/usr/bin/python3
"""square.Square class unit tests"""


import unittest
import inspect
from models import square, base
from contextlib import redirect_stdout
import io
import json
import os


class TestSquareDocstrings(unittest.TestCase):
    """square.Square class documentation"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.square_funcs = inspect.getmembers(
            square.Square, inspect.isfunction)

    def test_module_docstring(self):
        """Test Module documentation"""
        self.assertTrue(len(square.__doc__) > 0)

    def test_class_docstring(self):
        """Test Class documentation"""
        self.assertTrue(len(square.Square.__doc__) > 0)

    def test_func_docstrings(self):
        """Full scale doc strings"""
        for func in self.square_funcs:
            self.assertTrue(len(func[1].__doc__) > 0)
