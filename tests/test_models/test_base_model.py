#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
    """

    def test_base_model_creation(self):
        """
        Test the creation of a BaseModel instance.
        """
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertTrue(hasattr(bm, 'id'))
        self.assertTrue(hasattr(bm, 'created_at'))
        self.assertTrue(hasattr(bm, 'updated_at'))
        self.assertEqual(type(bm.id), str)
        self.assertEqual(type(bm.created_at), datetime)
        self.assertEqual(type(bm.updated_at), datetime)

    def test_base_model_str(self):
        """
        Test the string representation of a BaseModel instance.
        """
        bm = BaseModel()
        bm_str = str(bm)
        self.assertEqual(bm_str[1:12], "BaseModel]")
        self.assertIn("'id':", bm_str)
        self.assertIn("'created_at':", bm_str)
        self.assertIn("'updated_at':", bm_str)

    def test_base_model_save(self):
        """
        Test the save method of the BaseModel class.
        """
        bm = BaseModel()
        bm_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(bm.updated_at, bm_updated_at)
        self.assertTrue(hasattr(bm, 'id'))
        self.assertTrue(hasattr(bm, 'created_at'))
        self.assertTrue(hasattr(bm, 'updated_at'))
        self.assertEqual(type(bm.id), str)
        self.assertEqual(type(bm.created_at), datetime)
        self.assertEqual(type(bm.updated_at), datetime)

    def test_base_model_to_dict(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(type(bm_dict['id']), str)
        self.assertEqual(type(bm_dict['created_at']), str)
        self.assertEqual(type(bm_dict['updated_at']), str)

    def test_base_model_from_dict(self):
        """
        Test the from_dict method of the BaseModel class.
        """
        bm_dict = {
            '__class__': 'BaseModel',
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00'
        }
        bm = BaseModel.from_dict(bm_dict)
        self.assertIsInstance(bm, BaseModel)
        self.assertEqual(bm.id, '123')
        self.assertEqual(type(bm.created_at), datetime)
        self.assertEqual(type(bm.updated_at), datetime)


if __name__ == '__main__':
    unittest.main()
