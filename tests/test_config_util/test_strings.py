"""Module which contains the class to test methods
from the strings.py module."""
import unittest
from unittest import mock
from util import strings


class TestStrings(unittest.TestCase):
    """Class which tests methods from the strings.py module."""

    def setUp(self):
        """Sets up a new mock object for each test."""

        self.mock = mock.Mock()

    def test_get_config_metrics(self):
        """Tests if the values from the get_config_metrics
        method are the correct ones."""

        expected = {'disk_usage': 'YES',
                    'cpu_percent': 'YES',
                    'memory_info': 'YES',
                    'cpu_stats': 'YES'}

        actual = strings.get_config_metrics()

        self.assertEqual(expected, actual)

    def test_get_config_db(self):
        """Tests if the values from the get_config_db
        method are the correct ones."""

        expected = {'db_name': 'database_name',
                    'db_url': 'database_url'}

        actual = strings.get_config_db()

        self.assertEqual(expected, actual)

    def test_get_config_connection(self):
        """Tests if the values from the get_config_db
        method are the correct ones."""

        expected = {'send_time': '5',
                    'address': 'localhost',
                    'port': '5672',
                    'flask_port': '500'}

        actual = strings.get_config_connection()

        self.assertEqual(expected, actual)
