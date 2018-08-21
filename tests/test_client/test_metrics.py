"""Module which tests the metrics.py methods."""
import os
import unittest
from unittest import mock
from util import configurator, strings
import metrics


class TestMetrics(unittest.TestCase):
    """Class which contains methods to test
    the Metric class."""

    def setUp(self):
        """Initialises a mocker and a Metric object
        to be tested."""

        self.mock = mock.Mock()
        self.test = metrics.Metric()
        self.config = configurator.Config()

    def tearDown(self):
        """Creates a new config.ini file after each test."""

        self.config = configurator.Config()
        self.config.set_config()

    @mock.patch('util.reader.Reader')
    def test_validator_called(self, reader):
        """Tests the calling of Reader()"""

        self.mock.attach_mock(reader, 'Reader')
        self.test.__init__()

        expected = mock.call.Reader()
        actual = self.mock.mock_calls.pop(0)

        self.assertEqual(expected, actual)

    @mock.patch('client.metrics.Metric.get_memory_info')
    def test_get_values_set(self, get_cpu_stats):
        """Tests whether the get_value function only calls
        get_cpu_stats(), after the config.ini file has been
        set to have YES only to cpu_stats."""

        self.mock.attach_mock(get_cpu_stats, 'get_memory_info')

        print(self.test.get_values())

        print(self.mock.mock_calls)

    @mock.patch('psutil.disk_usage')
    def test_get_disk_usage(self, disk_usage):
        """Tests if the get_disk_usage method calls the correct
        psutil function."""

        self.mock.attach_mock(disk_usage, 'disk_usage')

        self.test.get_disk_usage()

        expected = mock.call.disk_usage(os.path.abspath(os.sep))
        actual = self.mock.mock_calls[0]

        self.assertEqual(expected, actual)

    @mock.patch('psutil.cpu_percent')
    def test_get_cpu_percent(self, cpu_percent):
        """Tests if the get_cpu_percent method calls the correct
        psutil function."""

        self.mock.attach_mock(cpu_percent, 'cpu_percent')

        self.test.get_cpu_percent()

        expected = mock.call.cpu_percent(interval=1, percpu=True)
        actual = self.mock.mock_calls[0]

        self.assertEqual(expected, actual)

    @mock.patch('psutil.virtual_memory')
    def test_get_memory_info(self, virtual_memory):
        """Tests if the get_memory_info method calls the correct
        psutil function."""

        self.mock.attach_mock(virtual_memory, 'virtual_memory')

        self.test.get_memory_info()

        expected = mock.call.virtual_memory()
        actual = self.mock.mock_calls[0]

        self.assertEqual(expected, actual)

    @mock.patch('psutil.cpu_stats')
    def test_cpu_stats(self, cpu_stats):
        """Tests if the get_cpu_stats method calls the correct
        psutil function."""

        self.mock.attach_mock(cpu_stats, 'cpu_stats')

        self.test.get_cpu_stats()

        expected = mock.call.cpu_stats()
        actual = self.mock.mock_calls[0]

        self.assertEqual(expected, actual)
