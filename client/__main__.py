"""Main module, this starts the application"""

import packets
from util import identifier, configurator


if __name__ == '__main__':
    """Calls the configuration and checking of parser.txt.
    Starts reading packet and sending them to the RabbitMQ server."""

    configurator.Config()
    identifier.Identifier()
    send_pack = packets.Packet()
    send_pack.set_data()