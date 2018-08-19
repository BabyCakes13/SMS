"""Main module, this starts the application"""

from client.configuration import configurator, identifier
from client.packet import packets


def main():
    """Calls the configuration and checking of parser.txt.
        Starts reading packet and sending them to the RabbitMQ server."""

    configurator.Config()
    identifier.Identifier()
    packets.Packet()


if __name__ == '__main__':
    main()

