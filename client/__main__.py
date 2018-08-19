"""Main module, this starts the application"""

from config_util import identifier, configurator
from client.packet import packets


if __name__ == '__main__':
    """Calls the configuration and checking of parser.txt.
            Starts reading packet and sending them to the RabbitMQ server."""

    configurator.Config()
    identifier.Identifier()
    packets.Packet()