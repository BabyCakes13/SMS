"""Module which tests the functionality
of configurator.py"""
import re
import unittest
from unittest import mock
from client.configuration import configurator
from client.files import strings


class TestConfig(unittest.TestCase):
    """Class which tests the methods
    from Config class."""

    def setUp(self):
        """Calls the Config object to handle
        config.ini file."""

        self.mock = mock.Mock()
        self.test = configurator.Config()

    def tearDown(self):

        self.test.__init__()

    @mock.patch('client.configuration.configurator.Config.set_config')
    def test_set_config_called(self, set_config):
        """Tests if the set_config functions is called
        when the file is not valid."""

        self.mock.attach_mock(set_config, 'set_config')

        with open(strings.get_config_path(), "w") as file:
            file.write("Nonsense!")

        self.test.__init__()

        expected = mock.call.set_config()
        actual = self.mock.mock_calls.pop(0)

        self.assertEqual(expected, actual)

    @mock.patch('configparser.ConfigParser')
    def test_configparser_called(self, config):
        """Tests the calling of ConfigParser()"""

        self.mock.attach_mock(config, 'ConfigParser')
        self.test.__init__()

        expected = mock.call.ConfigParser()
        actual = self.mock.mock_calls.pop(0)

        self.assertEqual(expected, actual)

    @mock.patch('client.configuration.validator.Validator')
    def test_validator_called(self, validator):
        """Tests the calling of ConfigParser()"""

        self.mock.attach_mock(validator, 'Validator')
        self.test.__init__()

        expected = mock.call.Validator()
        actual = self.mock.mock_calls.pop(0)

        self.assertEqual(expected, actual)

    def test_set_config_true(self):
        """Tests whether the sections which should be existent
        in the config.ini file are there."""

        file = open(strings.get_config_path(), "r")

        actual = re.search('CONNECTION', file.read()).group()
        self.assertEqual('CONNECTION', actual)
        file.seek(0)
        actual = re.search('DATABASE', file.read()).group()
        self.assertEqual('DATABASE', actual)
        file.seek(0)
        actual = re.search('METRICS', file.read()).group()
        self.assertEqual('METRICS', actual)

        file.close()

    def test_set_config_false(self):
        """Sets the sections to be nonexistent and checks
        if the file is correctly handled."""

        with open(strings.get_config_path(), "w") as file:
            file.write("nonsense!")

        file = open(strings.get_config_path(), "r")

        self.assertIsNone(re.search('CONNECTION', file.read()))
        file.seek(0)
        self.assertIsNone(re.search('DATABASE', file.read()))
        file.seek(0)
        self.assertIsNone(re.search('METRICS', file.read()))

        file.close()
