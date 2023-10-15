#!/usr/bin/python3
"""
Unit tests for City class.
"""

import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for City class.
    """

    def test_city_creation(self):
        """
        Test the creation of a City instance.
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertEqual(type(city.id), str)
        self.assertEqual(type(city.created_at), datetime)
        self.assertEqual(type(city.updated_at), datetime)
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')

    def test_city_str(self):
        """
        Test the string representation of a City instance.
        """
        city = City()
        city_str = str(city)
        self.assertEqual(city_str[1:6], "City]")
        self.assertIn("'id':", city_str)
        self.assertIn("'created_at':", city_str)
        self.assertIn("'updated_at':", city_str)
        self.assertIn("'state_id':", city_str)
        self.assertIn("'name':", city_str)

    def test_city_attributes_assignment(self):
        """
        Test the assignment of attributes of the City class.
        """
        city = City()
        city.state_id = '123'
        city.name = 'San Francisco'
        self.assertEqual(city.state_id, '123')
        self.assertEqual(city.name, 'San Francisco')

    def test_city_to_dict(self):
        """
        Test the 'to_dict' method of the City class.
        """
        city = City()
        city.state_id = '123'
        city.name = 'San Francisco'
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(type(city_dict['id']), str)
        self.assertEqual(type(city_dict['created_at']), str)
        self.assertEqual(type(city_dict['updated_at']), str)
        self.assertEqual(type(city_dict['state_id']), str)
        self.assertEqual(type(city_dict['name']), str)
        self.assertEqual(city_dict['state_id'], '123')
        self.assertEqual(city_dict['name'], 'San Francisco')

    def test_city_from_dict(self):
        """
        Test the 'from_dict' method of the City class.
        """
        city_dict = {
            '__class__': 'City',
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            'state_id': '456',
            'name': 'Los Angeles'
        }
        city = City.from_dict(city_dict)
        self.assertIsInstance(city, City)
        self.assertEqual(city.id, '123')
        self.assertEqual(type(city.created_at), datetime)
        self.assertEqual(type(city.updated_at), datetime)
        self.assertEqual(city.state_id, '456')
        self.assertEqual(city.name, 'Los Angeles')


if __name__ == '__main__':
    unittest.main()
