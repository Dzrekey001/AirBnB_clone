#!/usr/bin/python3
"""
Unit tests for Place class.
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for Place class.
    """

    def test_place_creation(self):
        """
        Test the creation of a Place instance.
        """
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertEqual(type(place.id), str)
        self.assertEqual(type(place.created_at), datetime)
        self.assertEqual(type(place.updated_at), datetime)
        self.assertEqual(place.city_id, '')
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.name, '')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_str(self):
        """
        Test the string representation of a Place instance.
        """
        place = Place()
        place_str = str(place)
        self.assertEqual(place_str[1:7], "Place]")
        self.assertIn("'id':", place_str)
        self.assertIn("'created_at':", place_str)
        self.assertIn("'updated_at':", place_str)
        self.assertIn("'city_id':", place_str)
        self.assertIn("'user_id':", place_str)
        self.assertIn("'name':", place_str)
        self.assertIn("'description':", place_str)
        self.assertIn("'number_rooms':", place_str)
        self.assertIn("'number_bathrooms':", place_str)
        self.assertIn("'max_guest':", place_str)
        self.assertIn("'price_by_night':", place_str)
        self.assertIn("'latitude':", place_str)
        self.assertIn("'longitude':", place_str)
        self.assertIn("'amenity_ids':", place_str)

    def test_place_attributes_assignment(self):
        """
        Test the assignment of attributes of the Place class.
        """
        place = Place()
        place.city_id = '123'
        place.user_id = '456'
        place.name = 'Cozy House'
        place.description = 'A charming place to stay'
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ['1', '2', '3']
        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')
        self.assertEqual(place.name, 'Cozy House')
        self.assertEqual(place.description, 'A charming place to stay')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ['1', '2', '3'])

    def test_place_to_dict(self):
        """
        Test the 'to_dict' method of the Place class.
        """
        place = Place()
        place.city_id = '123'
        place.user_id = '456'
        place.name = 'Cozy House'
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(type(place_dict['id']), str)
        self.assertEqual(type(place_dict['created_at']), str)
        self.assertEqual(type(place_dict['updated_at']), str)
        self.assertEqual(type(place_dict['city_id']), str)
        self.assertEqual(type(place_dict['user_id']), str)
        self.assertEqual(type(place_dict['name']), str)
        self.assertEqual(place_dict['city_id'], '123')
        self.assertEqual(place_dict['user_id'], '456')
        self.assertEqual(place_dict['name'], 'Cozy House')

    def test_place_from_dict(self):
        """
        Test the 'from_dict' method of the Place class.
        """
        place_dict = {
            '__class__': 'Place',
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            'city_id': '456',
            'user_id': '789',
            'name': 'Beach House'
        }
        place = Place.from_dict(place_dict)
        self.assertIsInstance(place, Place)
        self.assertEqual(place.id, '123')
        self.assertEqual(type(place.created_at), datetime)
        self.assertEqual(type(place.updated_at), datetime)
        self.assertEqual(place.city_id, '456')
        self.assertEqual(place.user_id, '789')
        self.assertEqual(place.name, 'Beach House')

if name == 'main':
    unittest.main()
