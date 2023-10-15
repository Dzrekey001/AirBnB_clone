#!/usr/bin/python3
"""
Unit tests for User class.
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for User class.
    """

    def test_user_creation(self):
        """
        Test the creation of a User instance.
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertEqual(type(user.id), str)
        self.assertEqual(type(user.created_at), datetime)
        self.assertEqual(type(user.updated_at), datetime)
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_user_str(self):
        """
        Test the string representation of a User instance.
        """
        user = User()
        user_str = str(user)
        self.assertEqual(user_str[1:6], "User]")
        self.assertIn("'id':", user_str)
        self.assertIn("'created_at':", user_str)
        self.assertIn("'updated_at':", user_str)
        self.assertIn("'email':", user_str)
        self.assertIn("'password':", user_str)
        self.assertIn("'first_name':", user_str)
        self.assertIn("'last_name':", user_str)

    def test_user_attributes_assignment(self):
        """
        Test the assignment of attributes of the User class.
        """
        user = User()
        user.email = 'test@example.com'
        user.password = 'password123'
        user.first_name = 'John'
        user.last_name = 'Doe'
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_user_to_dict(self):
        """
        Test the 'to_dict' method of the User class.
        """
        user = User()
        user.email = 'test@example.com'
        user.password = 'password123'
        user.first_name = 'John'
        user.last_name = 'Doe'
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(type(user_dict['id']), str)
        self.assertEqual(type(user_dict['created_at']), str)
        self.assertEqual(type(user_dict['updated_at']), str)
        self.assertEqual(type(user_dict['email']), str)
        self.assertEqual(type(user_dict['password']), str)
        self.assertEqual(type(user_dict['first_name']), str)
        self.assertEqual(type(user_dict['last_name']), str)
        self.assertEqual(user_dict['email'], 'test@example.com')
        self.assertEqual(user_dict['password'], 'password123')
        self.assertEqual(user_dict['first_name'], 'John')
        self.assertEqual(user_dict['last_name'], 'Doe')

    def test_user_from_dict(self):
        """
        Test the 'from_dict' method of the User class.
        """
        user_dict = {
            '__class__': 'User',
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User.from_dict(user_dict)
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, '123')
        self.assertEqual(type(user.created_at), datetime)
        self.assertEqual(type(user.updated_at), datetime)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')


if __name__ == '__main__':
    unittest.main()
