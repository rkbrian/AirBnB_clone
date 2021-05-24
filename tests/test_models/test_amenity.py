#!/usr/bin/python3
"""
Module to supplement a unittest for module amenity.py
use with the following commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_amenity.py
"""

import unittest
from models import amenity
Amenity = amenity.Amenity
from models.base_model import BaseModel
import inspect
import pep8

# Test class inherits from unittest
class TestAmenityDoc(unittest.TestCase):
    """documentation tests for ``Amenity`` class"""

    @classmethod
    def setUpClass(cls):
        """method to prepare test fixture"""
        cls.amenity_f = inspect.getmembers(amenity, inspect.isfunction)

    def test_AmenityModule_doc(self):
        """method to test if module is properly documented"""
        self.assertIsNot(amenity.__doc__, None, 'module [amenity.py] should have\
                        proper documentation')
        self.assertTrue(len(amenity.__doc__) >= 1, 'module [amenity.py] should have\
                        proper documentation')

    def test_AmenityClass_doc(self):
        """method to test if class is properly documented"""
        self.assertIsNot(amenity.__doc__, None, 'definition of [Amenity] class should\
                        have proper documentation')
        self.assertTrue(len(amenity.__doc__) >= 1, 'definition of [Amenity] class\
                            should have proper documentation')

class TestAmenityFunctionality(unittest.TestCase):
    """functionality of ``Amenity``class"""

    def test_AmenitySubclass(self):
        """method to test if ``Amenity`` inherits from ``BaseModel``"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_AmenityName(self):
        """method to test if ``Amenity`` has name attribute and set to
        empty string"""
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, '')

