#!/usr/bin/python3
""" Function unit test: max_integer(list=[]) """


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_docstring_module(self):
        """Module docstring test"""
        module_doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_docstring_function(self):
        """Function docstring test"""
        func_doc = max_integer.__doc__
        self.assertTrue(len(func_doc) > 1)

    def test_noArgs(self):
        """In case no arguments are passed"""
        self.assertIsNone(max_integer())

    def test_noneArg(self):
        """ Incase none is passed """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_emptyList(self):
        """In case an empty list is passed """
        emptyList = []
        self.assertIsNone(max_integer(emptyList))

    def test_nonIntArg(self):
        """Tests for a non-int type in list"""
        any_list = [4, "two", 9, 9, 45, 4, "10"]
        with self.assertRaises(TypeError):
            max_integer(any_list)

    def test_oneMember(self):
        """In case one number is passed"""
        max_number = [5]
        self.assertEqual(max_integer(max_number), 5)

    def test_allNegArg(self):
        """ Incase of all numbers negative"""
        list_n = [-4, -5, -23, -34, -45]
        self.assertEqual(max_integer(list_n), -1)

    def test_endPositive(self):
        """Tests for max at the end of all positive"""
        end_pos = [4, 5, 3, 34, 45]
        self.assertEqual(max_integer(end_pos), 45)

    def test_middlePositive(self):
        """Tests for max in the middles of all positive """
        mid_pos = [4, 5, 250, 34, 45]
        self.assertEqual(max_integer(mid_pos), 250)

    def test_begPositive(self):
        """Tests for max at the beginning with all positive"""
        beg_pos = [120, 5, 3, 34, 45]
        self.assertEqual(max_integer(beg_pos), 120)

    def test_negOne(self):
        """Tests for one negative"""
        on_l = [46, 5, -3, 34, 45]
        self.assertEqual(max_integer(on_l), 46)

if __name__ == "__main__":
    unittest.main()
