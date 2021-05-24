#!/usr/bin/python3
"""
Module to supplement a unittest for class ``User``
use with the following commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_user.py
"""

import unittest
from models.user import User as user
from models.base_model import BaseModel
import inspect
import pep8
import os

# Test class inherits from unittest
class TestUserDoc(unittest.TestCase):
    """documentation tests for ``User`` class"""

    @classmethod
    def setUpClass(cls):
        """method to prepare test fixture"""
        cls.user = inspect.getmembers(user, inspect.isfunction)

    def test_UserModule_doc(self):
        """method to test if module is properly documented"""
        self.assertIsNot(user.__doc__, None, 'module [user.py] should have\
                        proper documentation')
        self.assertTrue(len(user.__doc__) >= 1, 'module [user.py] should have\
                        proper documentation')

    def test_UserClass_doc(self):
        """method to test if class is properly documented"""
        self.assertIsNot(user.__doc__, None, 'definition of [User] class should\
                        have proper documentation')
        self.assertTrue(len(user.__doc__) >= 1, 'definition of [User] class\
                            should have proper documentation')

    def test_UserFunctions__doc(self):
        """method to test if functions are properly documented"""
        for function in self.user:
            self.assertIsNot(function[1].__doc__, None, '{:s} method should be\
                            properly documented'.format(function[0]))
            self.assertTrue(len(function[1].__doc__) >= 1, '{:s} method should\
                            be properly documented'.format(function[0]))

class TestUserFunctionality(unittest.TestCase):
    """functionality of ``User``class"""

    #def test_UserSubclass(self):
    #    """method to test if ``User`` inherits from ``BaseModel``"""
     #   self.assertIsInstance(user, BaseModel)
      #  self.assertTrue(hasattr(user, 'id'))
       # self.assertTrue(hasattr(user, 'created_at'))
       # self.assertTrue(hasattr(user, 'updated_at'))

    def test_UserFirstName(self):
        """method to test if ``User`` has first_name attribute and set to
        empty string"""
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual(user.first_name, '')

    def test_UserLasName(self):
         """method to test if ``User`` has last_name attribute and set to
         empty string"""
         self.assertTrue(hasattr(user, 'first_name'))
         self.assertEqual(user.last_name, '')
    def test_UserPasswd(self):
        """method to test if ``User`` has password attribute and set to
        empty string"""
        self.assertTrue(hasattr(user, 'password'))
        self.assertEqual(user.password, '')
    def test_UserEmail(self):
        """method to test if ``User`` has email attribute and set to
        empty string"""
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual(user.email, '')

if __name__ == '__main__':
    unittest.main()
