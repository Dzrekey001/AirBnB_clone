#!/usr/bin/python3
"""
Unit tests for State class.
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for State class.
    """

    def test_state_creation(self):
        """
        Test the creation of a State instance.
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertEqual(type(state.id), str)
        self.assertEqual(type(state.created_at), datetime)
        self.assertEqual(type(state.updated_at), datetime)
        self.assertEqual(state.name, '')

    def test_state_str(self):
        """
        Test the string representation of a State instance.
        """
        state = State()
        state_str = str(state)
        self.assertEqual(state_str[1:7], "State]")
        self.assertIn("'id':", state_str)
        self.assertIn("'created_at':", state_str)
        self.assertIn("'updated_at':", state_str)
        self.assertIn("'name':", state_str)

    def test_state_attributes_assignment(self):
        """
        Test the assignment of attributes of the State class.
        """
        state = State()
        state.name = 'California'
        self.assertEqual(state.name, 'California')

    def test_state_to_dict(self):
        """
        Test the 'to_dict' method of the State class.
        """
        state = State()
        state.name = 'California'
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(type(state_dict['id']), str)
        self.assertEqual(type(state_dict['created_at']), str)
        self.assertEqual(type(state_dict['updated_at']), str)
        self.assertEqual(type(state_dict['name']), str)
        self.assertEqual(state_dict['name'], 'California')

    def test_state_from_dict(self):
        """
        Test the 'from_dict' method of the State class.
        """
        state_dict = {
            '__class__': 'State',
            'id': '123',
            'created_at': '2022-01-01T00:00:00',
            'updated_at': '2022-01-02T00:00:00',
            'name': 'California'
        }
        state = State.from_dict(state_dict)
        self.assertIsInstance(state, State)
        self.assertEqual(state.id, '123')
        self.assertEqual(type(state.created_at), datetime)
        self.assertEqual(type(state.updated_at), datetime)
        self.assertEqual(state.name, 'California')


if __name__ == '__main__':
    unittest.main()
