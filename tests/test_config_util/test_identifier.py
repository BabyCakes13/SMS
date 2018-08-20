"""Module which contains class TestIdentifier to test
identifier.py"""
import os
import unittest
from unittest import mock
from util import identifier, strings


class TestIdentifier(unittest.TestCase):
    """Class which tests Identifier methods."""

    def setUp(self):
        """Initialises the tester for the identifier.py module."""

        self.mock = mock.Mock()
        self.test = identifier.Identifier()

    def tearDown(self):
        """Sets the id to be the correct id."""

        self.test.set_id()

    @mock.patch('util.identifier.Identifier.set_id')
    def test_init_false(self, set_id):
        """Tests if init calls the set_id function if validate_id
        is False"""

        self.mock.attach_mock(set_id, 'set_id')

        with open(strings.get_id_path(), "w") as file:
            file.write("the dark side should have won.")

        self.test.__init__()

        expected = mock.call.set_id()
        actual = self.mock.mock_calls[0]

        self.assertEqual(expected, actual)

    @mock.patch('util.identifier.Identifier.set_id')
    def test_init_true(self, set_id):
        """Tests if init doesn't call the set_id function if validate_id
        is True"""

        self.mock.attach_mock(set_id, 'set_id')

        self.test.__init__()

        expected = []
        actual = self.mock.mock_calls

        self.assertEqual(expected, actual)

    def test_get_id_default(self):
        """Tests whether the get_id methods from identifier.py
        returns the correct result when the file is not altered."""

        expected = self.test.get_uuid()
        actual = self.test.get_id()

        self.assertEqual(expected, actual)

    def test_get_id_altered(self):
        """Tests whether the get_id method from identifier.py
        returns the correct result when the file is altered."""

        expected = self.test.get_uuid()

        with open(strings.get_id_path(), "w") as file:
            file.write("this is definitely not the correct uuid.")

        actual = self.test.get_id()

        self.assertEqual(expected, actual)

    def test_validate_id_default(self):
        """Tests whether the validate_id method returns the
        expected result given that the file exists and is valid."""

        self.test.set_id()

        expected = True
        actual = self.test.validate_id()

        self.assertEqual(expected, actual)

    def test_validate_id_altered(self):
        """Tests whether the validate_id method from identifier.py
        returns the correct result when the file is altered."""

        expected = False

        with open(strings.get_id_path(), "w") as file:
            file.write("this is definitely not a valid file.")

        actual = self.test.validate_id()

        self.assertEqual(expected, actual)

    def test_validate_id_nonexistent(self):
        """Tests whether the validate_id method from identifier.py
        returns the correct result when the file doesn't exist."""

        expected = False

        os.remove(strings.get_id_path())

        actual = self.test.validate_id()

        self.assertEqual(expected, actual)

    def test_set_id_nonexistent(self):
        """Tests whether the set_id method creates id.txt file
        after it has been removed."""

        expected = True

        os.remove(strings.get_id_path())
        self.test.set_id()

        actual = os.path.isfile(strings.get_id_path())

        self.assertEqual(expected, actual)
