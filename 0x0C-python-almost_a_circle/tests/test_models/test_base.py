#!/usr/bin/python3
"""Base class unittest """


import unittest
import json
import inspect
from models import base
from models.base import Base


class TestBaseDocstrings(unittest.TestCase):
    """Base class unit tests"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_module_doc(self):
        """Test Module documentation"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """Test Class documentation"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_instance_id(self):
        """Test ids for class instances"""
        test1 = Base()
        self.assertEqual(test1.id, 1)

        bast_test = Base()
        self.assertEqual(bast_test.id, 2)

        test10 = Base(10)
        self.assertEqual(test10.id, 10)

        test3 = Base(12)
        self.assertEqual(test3.id, 3)

    def test_func_docstrings(self):
        """Tests for Docstrings"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) > 0)


class TestBase(unittest.TestCase):
    """Tests for Base class functionality """

    def test_excess_args(self):
        """ In case more arguments passed"""
        with self.assertRaises(TypeError):
            base_test = Base(1, 1)

    def test_no_id(self):
        """ In case no Id is passed """
        base_test = Base()
        self.assertEqual(base_test.id, 1)

    def test_specific_id(self):
        """Incase base ID is passed """
        base_test = Base(50)
        self.assertEqual(base_test.id, 50)

    def test_none_after_id(self):
        """None ID after not None"""
        bast_test = Base()
        self.assertEqual(bast_test.id, 2)

    def test_private_instance_att(self):
        """Private instances attribute test """
        base_test = Base(3)
        with self.assertRaises(AttributeError):
            print(base_test.__nb_objects)
        with self.assertRaises(AttributeError):
            print(base_test.nb_objects)

    def test_dumps(self):
        """Test dumps"""
        Base._Base__nb_objects = 0
        test_1 = {"id": 23, "width": 15, "height": 18, "x": 4, "y": 6}
        test_2 = {"id": 1, "width": 7, "height": 10, "x": 7, "y": 2}
        json_string = Base.to_json_string([test_1, test_2])
        self.assertTrue(type(json_string) is str)
        json_object = json.loads(json_string)
        self.assertEqual(json_object, [test_1, test_2])


if __name__ == '__main__':
    unittest.main()
