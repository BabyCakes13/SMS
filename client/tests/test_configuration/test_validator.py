"""Module which contains class to
test validator.py module."""
import os
import unittest
from client.configuration import configurator
from client.configuration import validator
from client.files import strings


class TestValidator(unittest.TestCase):
    """Class which contains methods for testing
    the validator.py module."""

    def setUp(self):
        """Initialises the validator and configurator
        for each test."""

        self.config = configurator.Config()
        self.test = validator.Validator()

    def tearDown(self):

        self.config.__init__()

    def test_check_values_true(self):
        """Given the correct file structure, checks
        whether the check_values returns the correct
        answer after verifying the values from
        config.ini."""

        actual = self.test.check_values()
        expected = True

        self.assertEqual(expected, actual)

    def test_check_values_false(self):
        """Given the incorrect file structure, checks
        whether the check_values returns the correct
        answer after verifying the values from
        config.ini."""

        with open(strings.get_config_path(), "w") as file:
            file.write("More nonsense.")

        actual = self.test.check_values()
        expected = False

        self.assertEqual(expected, actual)

    def test_check_keys_true(self):
        """Given the correct file structure, checks
        whether the check_keys returns the correct
        answer after verifying the keys from
        config.ini."""

        actual = self.test.check_keys()
        expected = True

        self.assertEqual(expected, actual)

    def test_check_keys_false(self):
        """Given the incorrect file structure, checks
        whether the check_keys returns the correct
        answer after verifying the keys from
        config.ini."""

        with open(strings.get_config_path(), "w") as file:
            file.write("More nonsense.")

        actual = self.test.check_keys()
        expected = False

        self.assertEqual(expected, actual)

    def test_check_config_true(self):
        """Given the correct file structure, checks
        whether the check_config returns the correct
        answer."""

        actual = self.test.check_config()
        expected = True

        self.assertEqual(expected, actual)

    def test_check_config_false(self):
        """First, given the incorrect file structure,
        checks whether the check_config method returns
        the expected result. Second, given the deleted file,
        checks for the same result."""

        with open(strings.get_config_path(), "w") as file:
            file.write("More nonsense.")

        actual = self.test.check_config()
        expected = False

        self.assertEqual(expected, actual)

        os.remove(strings.get_config_path())

        actual = self.test.check_config()
        expected = False

        self.assertEqual(expected, actual)




