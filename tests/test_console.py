#!/usr/bin/python3
"""Unittest module for the console.py"""

import unittest
from unittest.mock import patch
import io
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Defines all the classes for the console"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    @patch('sys.stdout', new=io.StringIO())
    def test_quit(self, mock_stdout):
        """Test do_quit() method"""
        self.assertTrue(self.console.onecmd("quit"))
        self.assertTrue(mock_stdout.getvalue() == '\n')

    @patch('sys.stdout', new=io.StringIO())
    def test_create_missing_class(self, mock_stdout):
        """Test do_create() method with missing class name"""
        self.console.do_create("")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_create_invalid_class(self, mock_stdout):
        """Test do_create() method with invalid class name"""
        self.console.do_create("InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_create_valid_class(self, mock_stdout):
        """Test do_create() method with valid class name"""
        self.console.do_create("BaseModel")
        obj_id = mock_stdout.getvalue().strip()
        self.assertIsNotNone(obj_id)

    @patch('sys.stdout', new=io.StringIO())
    def test_show_missing_class(self, mock_stdout):
        """Test do_show() method with missing class name"""
        self.console.do_show("")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_show_invalid_class(self, mock_stdout):
        """Test do_show() method with invalid class name"""
        self.console.do_show("InvalidClass 123")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_show_missing_id(self, mock_stdout):
        """Test do_show() method with missing instance ID"""
        self.console.do_show("BaseModel")
        self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_show_invalid_id(self, mock_stdout):
        """Test do_show() method with invalid instance ID"""
        self.console.do_show("BaseModel 123")
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_destroy_missing_class(self, mock_stdout):
        """Test do_destroy() method with missing class name"""
        self.console.do_destroy("")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_destroy_invalid_class(self, mock_stdout):
        """Test do_destroy() method with invalid class name"""
        self.console.do_destroy("InvalidClass 123")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_destroy_missing_id(self, mock_stdout):
        """Test do_destroy() method with missing instance ID"""
        self.console.do_destroy("BaseModel")
        self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_destroy_invalid_id(self, mock_stdout):
        """Test do_destroy() method with invalid instance ID"""
        self.console.do_destroy("BaseModel 123")
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_count_missing_class(self, mock_stdout):
        """Test do_count() method with missing class name"""
        self.console.do_count("")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_count_invalid_class(self, mock_stdout):
        """Test do_count() method with invalid class name"""
        self.console.do_count("InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_all_invalid_class(self, mock_stdout):
        """Test do_all() method with invalid class name"""
        self.console.do_all("InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_all_objects_by_class(self, mock_stdout):
        """Test do_all() method with class name"""
        self.console.do_all("BaseModel")
        self.assertNotEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new=io.StringIO())
    def test_all_all_objects(self, mock_stdout):
        """Test do_all() method without class name"""
        self.console.do_all("")
        self.assertNotEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new=io.StringIO())
    def test_update_missing_class(self, mock_stdout):
        """Test do_update() method with missing class name"""
        self.console.do_update("")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_update_invalid_class(self, mock_stdout):
        """Test do_update() method with invalid class name"""
        self.console.do_update("InvalidClass 123")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_update_missing_id(self, mock_stdout):
        """Test do_update() method with missing instance ID"""
        self.console.do_update("BaseModel")
        self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_update_invalid_id(self, mock_stdout):
        """Test do_update() method with invalid instance ID"""
        self.console.do_update("BaseModel 123")
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_update_missing_attribute(self, mock_stdout):
        """Test do_update() method with missing attribute"""
        self.console.do_update("BaseModel 123")
        self.assertEqual(mock_stdout.getvalue(), "** attribute name missing **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_update_missing_value(self, mock_stdout):
        """Test do_update() method with missing value"""
        self.console.do_update('BaseModel 123 attr')
        self.assertEqual(mock_stdout.getvalue(), "** value missing **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_update_valid_inputs(self, mock_stdout):
        """Test do_update() method with valid inputs"""
        self.console.do_create("BaseModel")
        obj_id = mock_stdout.getvalue().strip()

        # Update the BaseModel object with valid inputs
        self.console.do_update('BaseModel ' + obj_id + ' name "New Name"')
        updated_obj = storage.all()['BaseModel.' + obj_id]
        self.assertEqual(updated_obj.name, "New Name")

    @patch('sys.stdout', new=io.StringIO())
    def test_update_dict_missing_class(self, mock_stdout):
        """Test update_dict() method with missing class name"""
        self.console.update_dict("", "123", "{}")
        self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_update_dict_invalid_class(self, mock_stdout):
        """Test update_dict() method with invalid class name"""
        self.console.update_dict("InvalidClass", "123", "{}")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_update_dict_missing_id(self, mock_stdout):
        """Test update_dict() method with missing instance ID"""
        self.console.update_dict("BaseModel", "", "{}")
        self.assertEqual(mock_stdout.getvalue(), "** instance id missing **\n")

    @patch('sys.stdout', new=io.StringIO())
    def test_update_dict_invalid_id(self, mock_stdout):
        """Test update_dict() method with invalid instance ID"""
        self.console.update_dict("BaseModel", "123", "{}")
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")


if __name__ == '__main__':
    unittest.main()
