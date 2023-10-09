#!/usr/bin/env python3
""" BaseModel test suit

Unittest classes:
    TestBase_instantiation
    TestBase_save
    TestBase_to_dict
    TestBase_str
"""
import os
import unittest
from models.base_model import BaseModel

class TestBase_instantiation(unittest.TestCase):
    """Unittests of instantiation of the BaseModel class"""
    def test_with_args(self):
        with self.assertRaises(Exception)
        x = BaseModel(10, "youssef")
        print(x)

class TestBase_str(unittest.TestCase):
    """Unittests of str method of BaseModel class"""

    def test_return_type(self):
        x = BaseModel()
        self.assertIs(str, type(x.__str__()))

class TestBase_save(unittest.TestCase):
    """Unittests of save method"""

    def test_save(self):
        x = BaseModel()
        x_dict = x.to_dict().copy()
        x.save()
        x_saved_dict = x.to_dict().copy()
        self.assertNotEqual(x_dict, x_saved_dict)

class TestBase_to_dict(unittest.TestCase):
    """Unittests of to_dict method"""

    def test_to_dict_return_type(self):
        x = BaseModel()
        self.assertIs(type(x.to_dict()), dict)

    def test_to_dict_length(self):
        x = BaseModel()
        x.name = "BaseModel"
        _dict = x.to_dict()
        self.assertEqual(len(_dict), 5)

    def test_to_dict_with_str(self):
        x = BaseModel()
        x.name = "BaseModel"
        self.assertNotEqual(x.to_dict(), x.__dict__())


if __name__ == "__main__":
    unittest.main()
