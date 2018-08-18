"""Module which contains class to validate parser.ini."""
import os
import re
import configparser
from client.files import strings


class Validator:
    """Class which validates the structure
    of parser.ini."""

    def __init__(self):
        """Initialises the configurator passed
        by the Config class."""

        self.config = configparser.ConfigParser()

    def check_config(self):
        """Checks if the parser.ini file exists and
        valid. If it isn't, it creates a new one."""

        is_file = os.path.isfile(strings.get_config_path())

        if is_file:

            valid_keys = self.check_keys()
            valid_values = self.check_values()

            return valid_keys and valid_values

        return is_file

    def check_keys(self):
        """Checks whether the read sections
        are correct."""

        try:
            self.config.read(strings.get_config_path())
            keys = (self.config.options('CONNECTION') +
                    self.config.options('DATABASE') +
                    self.config.options('METRICS'))
        except configparser.Error:
            return False

        expected = list({**strings.get_config_connection(),
                         **strings.get_config_db(),
                         **strings.get_config_metrics()}.keys())

        return keys == expected

    def check_values(self):
        """Checks whether the options for CONNECTION
        and METRICS sections are valid"""

        try:
            self.config.read(strings.get_config_path())
            values = list({**dict(self.config.items('CONNECTION')),
                           **dict(self.config.items('METRICS'))}.values())
        except configparser.Error:
            return False

        expected = list(strings.get_values_re())

        for i, value in enumerate(values):
            if re.search(expected[i], value) is None:
                return False

        return True
