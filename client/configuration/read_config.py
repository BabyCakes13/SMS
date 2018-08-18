"""Module which reads the information from the parser.txt file:
metric options, send time, ip and address."""
import os
import re
from client.files import strings


class ReaderHandler:
    """Class which handles reading metrics from the configuration file"""

    def __init__(self):
        """Contains the path to the parser.txt file."""

        path = os.path.dirname(
            os.path.abspath(os.path.abspath(__file__)))[:-14]
        self.config_path = path + "\\files\\parser.txt"

    def get_metrics(self):
        """Returns the chosen option for the
        metrics in the configuration file."""

        print(self.config_path)

        f_config = open(self.config_path, "r")

        metric_group = re.search(strings.get_metrics_re(), f_config.read())

        metrics = [metric_group.group(1),
                   metric_group.group(2),
                   metric_group.group(3),
                   metric_group.group(4)]

        f_config.close()
        return metrics

    def get_address(self):
        """Returns the address on which the rabbitmq
         erver connects. It is localhost by default."""
        f_config = open(self.config_path, "r")

        address = re.search(strings.get_address_re(), f_config.read()).group()[8:]

        f_config.close()
        return address

    def get_port(self):
        """Returns the port which the rabbitmq
        server uses to connect. Default 5672."""
        f_config = open(self.config_path, "r")

        port = re.search(strings.get_port_re(), f_config.read()).group()[5:]

        f_config.close()
        return port

    def get_send_time(self):
        """Returns the send_time variable set in configuration file."""
        f_config = open(self.config_path, "r")

        send_time = re.search(strings.get_send_time_re(), f_config.read()).group()[-2:]

        f_config.close()
        return send_time
