"""Module which contains the class to test rabbitmq.py"""
import unittest
from client import rabbitmq
from util import reader


class TestRabbitMQ(unittest.TestCase):
    """Tests the rabbitmq.py module"""

    def setUp(self):
        """Creates a new connection for each test."""

        read = reader.Reader()
        self.test = rabbitmq.RabbitMQ(read.get_c_value()[1],
                                      read.get_c_value()[2])

    def test_init(self):
        """Tests that the connection is successful given the
        correct address and port."""

        result = self.test.rabbit_connection

        self.assertIsNotNone(result)

