#!/usr/bin/python3
"""
Module to supplement a unittest for class ``Review``
use with the following commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_review.py
"""

import unittest
from models.review import Review as review
from models.base_model import BaseModel
import inspect
import pep8

# Test class inherits from unittest
class TestReviewDoc(unittest.TestCase):
    """documentation tests for ``Review`` class"""

    @classmethod
    def setUpClass(cls):
        """method to prepare test fixture"""
        cls.review = inspect.getmembers(review, inspect.isfunction)

    def test_ReviewModule_doc(self):
        """method to test if module is properly documented"""
        self.assertIsNot(review.__doc__, None, 'module [review.py] should have\
                        proper documentation')
        self.assertTrue(len(review.__doc__) >= 1, 'module [review.py] should have\
                        proper documentation')

    def test_ReviewClass_doc(self):
        """method to test if class is properly documented"""
        self.assertIsNot(review.__doc__, None, 'definition of [Review] class should\
                        have proper documentation')
        self.assertTrue(len(review.__doc__) >= 1, 'definition of [Review] class\
                            should have proper documentation')

    def test_ReviewFunctions__doc(self):
        """method to test if functions are properly documented"""
        for function in self.review:
            self.assertIsNot(function[1].__doc__, None, '{:s} method should be\
                            properly documented'.format(function[0]))
            self.assertTrue(len(function[1].__doc__) >= 1, '{:s} method should\
                            be properly documented'.format(function[0]))

class TestReviewFunctionality(unittest.TestCase):
    """functionality of ``Review``class"""

    def test_ReviewSubclass(self):
        """method to test if ``Review`` inherits from ``BaseModel``"""
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))

    def test_ReviewPlaceId(self):
        """method to test if ``Review`` has place_id attribute and set to
        empty string"""
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, '')

    def test_ReviewUserId(self):
        """method to test if ``Review`` has state_id attribute and set to
        empty string"""
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, '')

    def test_ReviewText(self):
        """method to test if ``Review`` has text section attribute and set to
        empty string"""
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, '')

if __name__ == '__main__':
    unittest.main()
