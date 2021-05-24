#!/usr/bin/python3
"""unittest for FileStorage"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import os
import inspect
import pep8
Storage = FileStorage()

class TestFileStorage(unittest.TestCase):
    """defining the unittest cases for FileStorage class"""

    path = Storage._FileStorage__file_path
    @classmethod
    def setUpClass(cls):
        """collect members of the class for the doc tests"""
        cls.setup = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance(self):
        """method to test conformity to PEP8."""
        p8_syle = pep8.StyleGuide(quiet=True)
        checks = p8_syle.check_files(["./models/base_model.py"])
        self.assertEqual(checks.total_errors, 0, "Found code style errors.")

    def test_StorageModuleDoc(self):
        """method to test docstring doc for module"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_StorageclassDoc(self):
        """method to test docstring doc for classes"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_StorageFuncDoc(self):
        """method to test docstring doc for functions"""
        for each in self.setup:
            self.assertTrue(len(each[1].__doc__) >= 1)

    def test_StorageAll(self):
        """method to test the path and dict"""
        if os.path.exists(self.path):
            os.remove(self.path)
        self.assertIsInstance(Storage.all(), dict)

    def test_StorageNew(self):
        """method to test if objects are being set with respective keys"""
        models = Storage.all().copy()
        model = BaseModel()
        self.assertEqual(models, Storage.all())

    def test_StorageSave(self):
        """method to test serialization"""
        if os.path.exists(self.path):
            os.remove(self.path)
        models = BaseModel()
        models.save()
        self.assertNotEqual(os.path.getsize(self.path), 0)

    def test_StorageDict(self):
        """method to test dictionary"""
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_StorageReload(self):
        """method to test for deserialization"""
        if os.path.exists(self.path):
            os.remove(self.path)
        model = BaseModel()
        model.save()
        Storage.reload()
        my_dict = Storage.all().copy()
        model.val = 100
        self.assertEqual(model.val, 100)
        Storage.reload()
        self.assertNotEqual(Storage.all(), my_dict)

if __name__ == '__main__':
    unittest.main()
