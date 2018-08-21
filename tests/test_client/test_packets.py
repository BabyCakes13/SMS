"""Module which contains class to test packets.py module."""
import unittest
from unittest import mock
import packets
from util import configurator, strings


class TestPacket(unittest.TestCase):
    """Class which contains methods to test the
    packets.py module in client."""

    def setUp(self):
        """Sets up new mock and test objects for each test."""

        self.mock = mock.Mock()
        self.test = packets.Packet()
        self.config = configurator.Config()
        self.config.set_config()

    def tearDown(self):
        """After each test, a new CONFIG.ini file is created."""

        self.config = configurator.Config()
        self.config.set_config()

    @mock.patch('client.packets.Packet.set_connection')
    @mock.patch('util.identifier.Identifier.get_id')
    @mock.patch('util.identifier.Identifier')
    @mock.patch('util.reader.Reader')
    def test_init(self, reader, identifier, get_id, set_connection):
        """Tests if the init functions are called in
        the correct order."""

        self.mock.attach_mock(reader, 'Reader')
        self.mock.attach_mock(identifier, 'Identifier')
        self.mock.attach_mock(get_id, 'get_id')
        self.mock.attach_mock(set_connection, 'set_connection')

        self.test.__init__()

        expected = [mock.call.Reader(),
                    mock.call.Identifier(),
                    mock.call.Identifier().get_id(),
                    mock.call.set_connection()]

        actual = self.mock.mock_calls

        self.assertEqual(expected, actual)

    def test_set_connection_default(self):
        """Tests whether the connection to the RabbitMQ queue
        is successful after configuring a new CONFIG.ini file."""

        self.config.set_config()

        result = self.test.set_connection()

        self.assertIsNotNone(result)

    def test_set_connection_altered(self):
        """Tests whether the connection to the RabbitMQ queue
        is successful after altering the address and port found
        in CONFIG.ini file."""

        self.config.parser.read(strings.get_config_path())
        self.config.parser.set('CONNECTION', 'address', 'bad coffee')
        self.config.parser.set('CONNECTION', 'port', 'not coffee')

        result = self.test.set_connection()

        self.assertIsNotNone(result)

    def test_start_sending_false(self):
        """Tests that if the connection to the RabbitMQ is None
        the loop ends."""

        self.test.start_sending(None)

        expected = []
        actual = self.mock.mock_calls

        self.assertEqual(expected, actual)
