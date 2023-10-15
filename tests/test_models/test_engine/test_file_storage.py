#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        cls.file_path = "test.json"
        cls.storage = FileStorage()
        cls.storage._FileStorage__file_path = cls.file_path

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove(cls.file_path)
        except FileNotFoundError:
            pass

    def setUp(self):
        self.storage.reload()
        self.obj = BaseModel()
        self.obj.save()

    def tearDown(self):
        self.storage._FileStorage__objects = {}
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        objects = self.storage.all()
        self.assertEqual(type(objects), dict)
        self.assertIn(self.obj.__class__.__name__ + "." + self.obj.id, objects)
        self.assertIs(objects[self.obj.__class__.__name__ + "." + self.obj.id], self.obj)

    def test_new(self):
        new_obj = BaseModel()
        new_obj.save()
        objects = self.storage.all()
        self.assertIn(new_obj.__class__.__name__ + "." + new_obj.id, objects)
        self.assertIs(objects[new_obj.__class__.__name__ + "." + new_obj.id], new_obj)

    def test_save(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)
        key = self.obj.__class__.__name__ + "." + self.obj.id
        self.assertIn(key, data)

    def test_reload(self):
        obj_id = self.obj.id
        self.storage.reload()
        objects = self.storage.all()
        self.assertNotIn(self.obj.__class__.__name__ + "." + obj_id, objects)

    def test_reload_from_nonexistent_file(self):
        os.remove(self.file_path)
        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(len(objects), 0)


if __name__ == "__main__":
    unittest.main()
