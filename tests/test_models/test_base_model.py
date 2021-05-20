#!/usr/bin/python3
"""unittest for BaseModel"""
from models.base_model import BaseModel
import unittest
import inspect
import pep8


class TestBaseModel(unittest.TestCase):
    """defining the unittest cases for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """collect members of the class for the doc tests"""
        cls.setup = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """method to test conformity to PEP8."""
        p8_syle = pep8.StyleGuide(quiet=True)
        checks = p8_syle.check_files(["./models/base_model.py"])
        self.assertEqual(checks.total_errors, 0, "Found code style errors "
                        + "(and warnings).")

    def test_pep8_conformance_test_BaseModel(self):
        """method to test this file to pep8 conformity"""
        p8_syle = pep8.StyleGuide(quiet=True)
        checks = p8_syle.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(checks.total_errors, 1, "Found code style errors "
                        + "(and warnings).")

    def test_module_docstring(self):
        """method to test docstring doc for module"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        """method to test docstring doc for classes"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """method to test docstring doc for functions"""
        for each in self.setup:
            self.assertTrue(len(each[1].__doc__) >= 1)
