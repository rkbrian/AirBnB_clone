#!/usr/bin/python3
"""
Module to supplement a unittest for class ``State``
use with the following commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_state.py
"""

import unittest
from models.state import State as state
from models.base_model import BaseModel
import inspect
import pep8

# Test class inherits from unittest
class TestStateDoc(unittest.TestCase):
    """documentation tests for ``State`` class"""

    @classmethod
    def setUpClass(cls):
        """method to prepare test fixture"""
        cls.state = inspect.getmembers(state, inspect.isfunction)

    def test_StateModule_doc(self):
        """method to test if module is properly documented"""
        self.assertIsNot(state.__doc__, None, 'module [state.py] should have\
                        proper documentation')
        self.assertTrue(len(state.__doc__) >= 1, 'module [state.py] should have\
                        proper documentation')

    def test_StateClass_doc(self):
        """method to test if class is properly documented"""
        self.assertIsNot(state.__doc__, None, 'definition of [State] class should\
                        have proper documentation')
        self.assertTrue(len(state.__doc__) >= 1, 'definition of [State] class\
                            should have proper documentation')

    def test_StateFunctions__doc(self):
        """method to test if functions are properly documented"""
        for function in self.state:
            self.assertIsNot(function[1].__doc__, None, '{:s} method should be\
                            properly documented'.format(function[0]))
            self.assertTrue(len(function[1].__doc__) >= 1, '{:s} method should\
                            be properly documented'.format(function[0]))

class TestStateFunctionality(unittest.TestCase):
    """functionality of ``State``class"""

    def test_StatetName(self):
        """method to test if ``State`` has name attribute and set to
        empty string"""
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, '')

if __name__ == '__main__':
    unittest.main()
