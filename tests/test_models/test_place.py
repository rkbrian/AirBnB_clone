#!/usr/bin/python3
"""
Module to supplement a unittest for class ``Place``
use with the following commands:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_place.py
"""

import unittest
from models.place import Place as place
from models.base_model import BaseModel
import inspect
import pep8

# Test class inherits from unittest
class TestPlaceDoc(unittest.TestCase):
    """documentation tests for ``Place`` class"""

    @classmethod
    def setUpClass(cls):
        """method to prepare test fixture"""
        cls.place = inspect.getmembers(place, inspect.isfunction)

    def test_PlaceModule_doc(self):
        """method to test if module is properly documented"""
        self.assertIsNot(place.__doc__, None, 'module [place.py] should have\
                        proper documentation')
        self.assertTrue(len(place.__doc__) >= 1, 'module [place.py] should have\
                        proper documentation')

    def test_PlaceClass_doc(self):
        """method to test if class is properly documented"""
        self.assertIsNot(place.__doc__, None, 'definition of [Place] class should\
                        have proper documentation')
        self.assertTrue(len(place.__doc__) >= 1, 'definition of [Place] class\
                            should have proper documentation')

    def test_PlaceFunctions__doc(self):
        """method to test if functions are properly documented"""
        for function in self.place:
            self.assertIsNot(function[1].__doc__, None, '{:s} method should be\
                            properly documented'.format(function[0]))
            self.assertTrue(len(function[1].__doc__) >= 1, '{:s} method should\
                            be properly documented'.format(function[0]))

class TestPlaceFunctionality(unittest.TestCase):
    """functionality of ``Place``class"""

    def test_PlacetName(self):
        """method to test if ``Place`` has name attribute and set to
        empty string"""
        self.assertTrue(hasattr(place, 'name'))
        self.assertEqual(place.name, '')

    def test_PlaceCityid(self):
        """method to test if ``Place`` has city_id attribute"""
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertIsInstance(place.city_id, str)

    def test_PlaceUserid(self):
        """method to test if ``Place`` has user_id attribute"""
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertIsInstance(place.user_id, str)

    def test_PlaceDescrption(self):
        """method to test if ``Place`` has description attribute"""
        self.assertTrue(hasattr(place, 'description'))
        self.assertEqual(place.description, '')

    def test_PlaceRoomCount(self):
        """method to test if ``Place`` has number_rooms attribute and set to 0
        """
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)

    def test_PlaceBathCount(self):
        """method to test if ``Place`` has number_bathrooms attribute and set
        to 0"""
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)

if __name__ == '__main__':
    unittest.main()
