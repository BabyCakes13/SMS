"""Module which creates the config.txt file if it does not exist
or it's invalid."""
import os
import re
from client.files import strings


class Configuration:
    """Class which handles the creation and validity of
    the configuration file."""

    def __init__(self):
        """Keeps the path to the config.txt file in config_path.
        If the config.txt file already exists and it valid,
        then it does nothing.
        Else, it creates a new default configuration file."""

        self.root_path = os.path.dirname(os.path.abspath(__file__))[:-14]
        self.config_path = os.path.join(self.root_path, "files\\config.txt")

        if self.check_configuration() is False:
            self.setup_configuration_file()

    def setup_configuration_file(self):
        """Creates the config.txt file, which contains the metrics
        which are possible to monitor.
        In order to deactivate one metric, write FALSE instead of TRUE"""

        with open(self.config_path, "w+") as f_config:

            f_config.write(strings.get_configuration_file_form())

    def validate_configuration_file(self):
        """Checks whether the structure of the configuration file is correct"""

        try:
            f_config = open(self.config_path, "r")
        except IOError:
            return False

        is_valid = \
            bool(re.search(strings.get_configuration_file_re(), f_config.read()))

        f_config.close()

        return is_valid

    def check_configuration(self):
        """Checks to see if the configuration file already exists and it's valid
        and creates another if it doesn't"""

        is_file = os.path.isfile(self.config_path)
        is_valid = self.validate_configuration_file()
        return bool(is_file and is_valid)
