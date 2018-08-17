"""Main module, this starts the application"""

from client.configuration import init_config, configurator
from client.metrics import packets


def initialise():
    """Calls the configuration and checking of config.txt.
    Starts reading metrics and sending them to the RabbitMQ server."""

    #init_config.initialise_configuration_id()

    config = configurator.Config()

    #packet_handler = packets.PacketHandler()
    #packet_handler.set_packet_data()


initialise()
