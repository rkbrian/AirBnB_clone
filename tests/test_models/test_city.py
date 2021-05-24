#!/usr/bin/python3
"""
Module to supplement a unittest for class ``City``
use with the following commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_city.py
"""

import unittest
from models.city import City as city
from models.base_model import BaseModel
import inspect
import pep8

# Test class inherits from unittest
class TestCityDoc(unittest.TestCase):
    """documentation tests for ``City`` class"""

    @classmethod
    def setUpClass(cls):
        """method to prepare test fixture"""
        cls.city = inspect.getmembers(city, inspect.isfunction)

    def test_CityModule_doc(self):
        """method to test if module is properly documented"""
        self.assertIsNot(city.__doc__, None, 'module [city.py] should have\
                        proper documentation')
        self.assertTrue(len(city.__doc__) >= 1, 'module [city.py] should have\
                        proper documentation')

    def test_CityClass_doc(self):
        """method to test if class is properly documented"""
        self.assertIsNot(city.__doc__, None, 'definition of [City] class should\
                        have proper documentation')
        self.assertTrue(len(city.__doc__) >= 1, 'definition of [City] class\
                            should have proper documentation')

    def test_CityFunctions__doc(self):
        """method to test if functions are properly documented"""
        for function in self.city:
            self.assertIsNot(function[1].__doc__, None, '{:s} method should be\
                            properly documented'.format(function[0]))
            self.assertTrue(len(function[1].__doc__) >= 1, '{:s} method should\
                            be properly documented'.format(function[0]))

class TestCityFunctionality(unittest.TestCase):
    """functionality of ``City``class"""

    def test_CitytName(self):
        """method to test if ``City`` has name attribute and set to
        empty string"""
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, '')

    def test_CityState(self):
        """method to test if ``City`` has state_id attribute and set to
        empty string"""
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, '')

if __name__ == '__main__':
    unittest.main()
