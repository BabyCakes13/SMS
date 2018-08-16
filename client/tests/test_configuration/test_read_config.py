"""Module which test whether the data found in
the config.txt is correctly read and handled."""
import unittest
import os
from client.configuration import read_config
from client.files import strings


class TestReadConfiguration(unittest.TestCase):
    """Tests if the input from the configuration
     file is correctly handled."""

    @classmethod
    def setUpClass(cls):
        cls.reader = read_config.ReaderHandler()
        cls.root_path = os.path.dirname(os.path.abspath(__file__))[:-24]
        cls.config_path = os.path.join(cls.root_path, "files\\config.txt")

    def test_get_metrics(self):
        """Tests if get_metrics() reads the options of the metrics
        from the configuration file correctly."""

        f_config = open(self.config_path, "w")
        f_config.write(strings.get_configuration_file_form())
        f_config.close()

        metric_values_1 = ['TRUE', 'TRUE', 'TRUE', 'TRUE']
        metric_values_2 = ['FALSE', 'TRUE', 'TRUE', 'TRUE']

        self.assertEqual(self.reader.get_metrics(), metric_values_1)
        self.assertNotEqual(self.reader.get_metrics(), metric_values_2)

    def test_get_address(self):
        """Tests if the get_address() reads the address correctly"""

        with open(self.config_path, "w") as f_config:
            f_config.write(strings.get_configuration_file_form())

        self.assertEqual(self.reader.get_address(), "localhost")
        self.assertNotEqual(self.reader.get_address(), "bad bad bad")

    def test_get_ip(self):
        """Tests if the get_ip() reads the ip correctly"""

        with open(self.config_path, "w") as f_config:
            f_config.write(strings.get_configuration_file_form())

        self.assertEqual(self.reader.get_port(), "5672")
        self.assertNotEqual(self.reader.get_port(), "666")

    def get_send_time(self):
        """Tests if the get_send_time() reads the send time correctly"""

        with open(self.config_path, "w") as f_config:
            f_config.write(strings.get_configuration_file_form())

        self.assertEqual(self.reader.get_send_time(), "2")
        self.assertNotEqual(self.reader.get_send_time(), "666")
