#!/usr/bin/python3
"""
Unit tests for Review class.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for Review class.
    """

    def test_review_creation(self):
        """
        Test the creation of a Review instance.
        """
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertEqual(type(review.id), str)
        self.assertEqual(type(review.created_at), datetime)
        self.assertEqual(type(review.updated_at), datetime)
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_review_str(self):
        """
        Test the string representation of a Review instance.
        """
        review = Review()
        review_str = str(review)
        self.assertEqual(review_str[1:8], "Review]")
        self.assertIn("'id':", review_str)
        self.assertIn("'created_at':", review_str)
        self.assertIn("'updated_at':", review_str)
        self.assertIn("'place_id':", review_str)
        self.assertIn("'user_id':", review_str)
        self.assertIn("'text':", review_str)

    def test_review_attributes_assignment(self):
        """
        Test the assignment of attributes of the Review class.
        """
        review = Review()
        review.place_id = '123'
        review.user_id = '456'
        review.text = 'Great place to stay!'
        self.assertEqual(review.place_id, '123')
        self.assertEqual(review.user_id, '456')
        self.assertEqual(review.text, 'Great place to stay!')

    def test_review_to_dict(self):
        """
        Test the 'to_dict' method of the Review class.
        """
        review = Review()
        review.place_id = '123'
        review.user_id = '456'
        review.text = 'Great place to stay!'
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(type(review_dict['id']), str)
        self.assertEqual(type(review_dict['created_at']), str)
        self.assertEqual(type(review_dict['updated_at']), str)
        self.assertEqual(type(review_dict['place_id']), str)
        self.assertEqual(type(review_dict['user_id']), str)
        self.assertEqual(type(review_dict['text']), str)
        self.assertEqual(review_dict['place_id'], '123')
        self.assertEqual(review_dict['user_id'], '456')
        self.assertEqual(review_dict['text'], 'Great place to stay!')

    def test_review_from_dict(self):
        """
        Test the 'from_dict' method of the Review class.
        """
        review_dict = {
            '__class__': 'Review',
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            'place_id': '456',
            'user_id': '789',
            'text': 'Amazing experience!'
        }
        review = Review.from_dict(review_dict)
        self.assertIsInstance(review, Review)
        self.assertEqual(review.id, '123')
        self.assertEqual(type(review.created_at), datetime)
        self.assertEqual(type(review.updated_at), datetime)
        self.assertEqual(review.place_id, '456')
        self.assertEqual(review.user_id, '789')
        self.assertEqual(review.text, 'Amazing experience!')


if __name__ == '__main__':
    unittest.main()
