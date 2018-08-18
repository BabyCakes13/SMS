"""Main module, this starts the application"""

from client.configuration import configurator, identifier
from client.packet import packets


def initialise():
    """Calls the configuration and checking of parser.txt.
    Starts reading packet and sending them to the RabbitMQ server."""

    configurator.Config()
    identifier.Identifier()
    packets.Packet()


initialise()

