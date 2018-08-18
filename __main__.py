"""Main module, this starts the application"""

from client.configuration import init_config, reader, configurator
from client.packet import packets
from client.packet import metrics


def initialise():
    """Calls the configuration and checking of parser.txt.
    Starts reading packet and sending them to the RabbitMQ server."""

    c = configurator.Config()
    packet_handler = packets.Packet()
    packet_handler.set_packet_data()


initialise()
