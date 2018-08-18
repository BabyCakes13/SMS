"""Main module, this starts the application"""

from client.configuration import init_config, reader, configurator
from client.metrics import packets


def initialise():
    """Calls the configuration and checking of parser.txt.
    Starts reading metrics and sending them to the RabbitMQ server."""

    config = configurator.Config()
    read = reader.Reader()

    """init_config.initialise_configuration_id()
    packet_handler = packets.PacketHandler()
    packet_handler.set_packet_data()"""


initialise()
