#!/usr/bin/python3
"""
Unit tests for Amenity class.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class.
    """

    def test_amenity_creation(self):
        """
        Test the creation of an Amenity instance.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertEqual(type(amenity.id), str)
        self.assertEqual(type(amenity.created_at), datetime)
        self.assertEqual(type(amenity.updated_at), datetime)
        self.assertEqual(amenity.name, '')

    def test_amenity_str(self):
        """
        Test the string representation of an Amenity instance.
        """
        amenity = Amenity()
        amenity_str = str(amenity)
        self.assertEqual(amenity_str[1:9], "Amenity]")
        self.assertIn("'id':", amenity_str)
        self.assertIn("'created_at':", amenity_str)
        self.assertIn("'updated_at':", amenity_str)
        self.assertIn("'name':", amenity_str)

    def test_amenity_name_assignment(self):
        """
        Test the assignment of the 'name' attribute.
        """
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_amenity_to_dict(self):
        """
        Test the 'to_dict' method of the Amenity class.
        """
        amenity = Amenity()
        amenity.name = "Gym"
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(type(amenity_dict['id']), str)
        self.assertEqual(type(amenity_dict['created_at']), str)
        self.assertEqual(type(amenity_dict['updated_at']), str)
        self.assertEqual(type(amenity_dict['name']), str)
        self.assertEqual(amenity_dict['name'], 'Gym')

    def test_amenity_from_dict(self):
        """
        Test the 'from_dict' method of the Amenity class.
        """
        amenity_dict = {
            '__class__': 'Amenity',
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            'name': 'Spa'
        }
        amenity = Amenity.from_dict(amenity_dict)
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.id, '123')
        self.assertEqual(type(amenity.created_at), datetime)
        self.assertEqual(type(amenity.updated_at), datetime)
        self.assertEqual(amenity.name, 'Spa')


if __name__ == '__main__':
    unittest.main()
