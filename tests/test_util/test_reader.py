"""Module which contains class to test
reader.py module."""
import unittest
from unittest import mock
from util import configurator, reader, strings


class TestReader(unittest.TestCase):
    """Class which tests the methods
    from Reader class."""

    def setUp(self):
        """Initialises the Reader object
        to be tested and Mock."""

        self.test = reader.Reader()
        self.config = configurator.Config()
        self.config.set_config()
        self.mock = mock.Mock()

    def tearDown(self):

        self.config.set_config()

    @mock.patch('configparser.ConfigParser')
    def test_init(self, parser):
        """Tests the calling of ConfigParser()"""

        self.mock.attach_mock(parser, 'ConfigParser')
        self.test.__init__()

        expected = mock.call.ConfigParser()
        actual = self.mock.mock_calls.pop(0)

        self.assertEqual(expected, actual)

    def test_get_m_value_default(self):
        """Tests that the values of METRICS section
        after rewriting parser.ini are the expected ones."""

        expected = ['YES', 'YES', 'YES', 'YES']
        actual = self.test.get_m_value()

        self.assertEqual(expected, actual)

        self.config.parser.set('METRICS', 'disk_usage', 'NO')

        with open(strings.get_config_path(), "w") as file:
            self.config.parser.write(file)

    def test_get_d_value_default(self):
        """Tests that the values of DATABASE section
        after rewriting parser.ini are the expected ones."""

        expected = ['database_name', 'database_url']
        actual = self.test.get_d_value()

        self.assertEqual(expected, actual)

    def test_get_c_value_default(self):
        """Tests that the values of CONNECTION section
        after rewriting parser.ini are the expected ones."""

        expected = ['5', 'localhost', '5672', '500']
        actual = self.test.get_c_value()

        self.assertEqual(expected, actual)

    def test_get_m_value_altered(self):
        """Tests that the values of METRICS section
        after altering parser.ini are the expected ones."""

        self.config.parser.set('METRICS', 'disk_usage', 'NO')

        with open(strings.get_config_path(), "w") as file:
            self.config.parser.write(file)

        expected = ['NO', 'YES', 'YES', 'YES']
        actual = self.test.get_m_value()

        self.assertEqual(expected, actual)

    def test_get_d_value_altered(self):
        """Tests that the values of DATABASE section
        after altering parser.ini are the expected ones."""

        self.config.parser.set('DATABASE', 'db_name', 'Mercy')

        with open(strings.get_config_path(), "w") as file:
            self.config.parser.write(file)

        expected = ['Mercy', 'database_url']
        actual = self.test.get_d_value()

        self.assertEqual(expected, actual)

    def test_get_c_value_altered(self):
        """Tests that the values of CONNECTION section
        after altering parser.ini are the expected ones."""

        self.config.parser.set('CONNECTION', 'send_time', '10')

        with open(strings.get_config_path(), "w") as file:
            self.config.parser.write(file)

        expected = ['10',
                    'localhost',
                    '5672',
                    '500']
        actual = self.test.get_c_value()

        self.assertEqual(expected, actual)

    def test_get_m_value_incorrect(self):
        """Tests that the values of METRICS section
        after altering parser.ini are the expected ones."""

        self.config.parser.set('METRICS', 'disk_usage', 'idk')

        with open(strings.get_config_path(), "w") as file:
            self.config.parser.write(file)

        expected = ['YES', 'YES', 'YES', 'YES']
        actual = self.test.get_m_value()

        self.assertEqual(expected, actual)

    def test_get_c_value_incorrect(self):
        """Tests that the values of CONNECTION section
        after altering parser.ini are the expected ones."""

        self.config.parser.set('CONNECTION', 'send_time', 'idk')

        with open(strings.get_config_path(), "w") as file:
            self.config.parser.write(file)

        expected = ['5',
                    'localhost',
                    '5672',
                    '500']
        actual = self.test.get_c_value()

        self.assertEqual(expected, actual)

    def test_get_m_keys_default(self):
        """Tests that the keys of METRICS section
        after rewriting parser.ini are the expected ones."""

        expected = ['disk_usage',
                    'cpu_percent',
                    'memory_info',
                    'cpu_stats']
        actual = self.test.get_m_keys()

        self.assertEqual(expected, actual)

    def test_get_d_keys_default(self):
        """Tests that the keys of DATABASE section
        after rewriting parser.ini are the expected ones."""

        expected = ['db_name', 'db_url']
        actual = self.test.get_d_keys()

        self.assertEqual(expected, actual)

    def test_get_c_keys_default(self):
        """Tests that the keys of CONNECTION section
        after rewriting parser.ini are the expected ones."""

        expected = ['send_time',
                    'address',
                    'port',
                    'flask_port']
        actual = self.test.get_c_keys()

        self.assertEqual(expected, actual)

    def test_get_m_keys_incorrect(self):
        """Tests that the values of METRICS section
        after altering parser.ini are the expected ones."""

        with open(strings.get_config_path(), "w") as file:
            file.write("Nonsense.")

        expected = ['YES', 'YES', 'YES', 'YES']
        actual = self.test.get_m_value()

        self.assertEqual(expected, actual)

    def test_get_d_keys_incorrect(self):
        """Tests that the values of DATABASE section
        after altering parser.ini are the expected ones."""

        with open(strings.get_config_path(), "w") as file:
            file.write("Nonsense.")

        expected = ['db_name', 'db_url']
        actual = self.test.get_d_keys()

        self.assertEqual(expected, actual)

    def test_get_c_keys_incorrect(self):
        """Tests that the keys of CONNECTION section
        after altering parser.ini are the expected ones."""

        with open(strings.get_config_path(), "w") as file:
            file.write("Nonsense.")

        expected = ['send_time',
                    'address',
                    'port',
                    'flask_port']
        actual = self.test.get_c_keys()

        self.assertEqual(expected, actual)
