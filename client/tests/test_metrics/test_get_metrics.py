"""Tests the correct working of the collect_metrics module"""
import os
import unittest
from unittest.mock import patch, Mock, call
from client.metrics import get_metrics


class TestCollectMetrics(unittest.TestCase):
    """Test class which checks the correct function
    of functions from collect_metrics module."""

    def setUp(self):
        """Initialises the metrics and mock objects."""

        self.metric_manager = get_metrics.Metrics()
        self.mock_manager = Mock()

    def test_get_metrics_values(self):
        """Tests the get_metrics_value function."""

        metrics = list(self.metric_manager.get_metrics_values().keys())
        expected_result = ['Disk_Usage',
                           'Cpu_Percent',
                           'Memory_Info',
                           'Cpu_Stats']

        for index, metrics in enumerate(metrics):
            self.assertEqual(metrics, expected_result[index])

    @patch('psutil.disk_usage')
    def test_disk_usage(self, disk_usage):
        """Tests if given the argument 0,
        the call_metric_function calls the right function."""

        self.mock_manager.attach_mock(disk_usage, 'disk_usage')
        expected_value = [call.disk_usage(os.path.abspath(os.sep))]

        self.metric_manager.call_metric_functions(0)
        self.assertEqual(self.mock_manager.mock_calls, expected_value)

    @patch('psutil.cpu_percent')
    def test_cpu_percent(self, cpu_percent):
        """Tests if given the argument 1,
        the call_metric_function calls the right function."""

        self.mock_manager.attach_mock(cpu_percent, 'cpu_percent')
        expected_value = [call.cpu_percent(interval=1, percpu=True)]

        self.metric_manager.call_metric_functions(1)
        self.assertEqual(self.mock_manager.mock_calls, expected_value)

    @patch('psutil.virtual_memory')
    def test_virtual_memory(self, cpu_percent):
        """Tests if given the argument 2,
        the call_metric_function calls the right function."""

        self.mock_manager.attach_mock(cpu_percent, 'virtual_memory')
        expected_value = [call.virtual_memory()]

        self.metric_manager.call_metric_functions(2)
        self.assertEqual(self.mock_manager.mock_calls, expected_value)

    @patch('psutil.cpu_stats')
    def test_cpu_stats(self, cpu_stats):
        """Tests if given the argument 3,
        the call_metric_function calls the right function."""

        self.mock_manager.attach_mock(cpu_stats, 'cpu_stats')
        expected_value = [call.cpu_stats()]

        self.metric_manager.call_metric_functions(3)
        self.assertEqual(self.mock_manager.mock_calls, expected_value)
