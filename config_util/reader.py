"""Module which contains Reader class to
get information from the parser.ini file."""
import configparser
from config_util import configurator, validator
from client.files import strings


class Reader:
    """Class which contains methods
    to get parser.ini info."""

    def __init__(self):
        """Initialises a parser to read the parser.ini
        file."""

        self.parser = configparser.ConfigParser()
        self.validator = validator.Validator()

    def validate_config(self):
        """Validates the parser.ini file before
        reading from it."""

        parser = configurator.Config()
        is_valid = self.validator.check_config()

        if is_valid is False:
            parser.set_config()

    def get_m_value(self):
        """Reads the values YES or NO from
        the parser.ini file, and returns a list
        with the answer for each metric.
        Returns a list with the values."""

        self.validate_config()

        self.parser.read(strings.get_config_path())

        metr = list(dict(self.parser.items('METRICS')).values())

        return metr

    def get_d_value(self):
        """Reads the values for db_name
        and db_url used to connect to
        database.
        Returns a list with the values."""

        self.validate_config()

        self.parser.read(strings.get_config_path())

        data = list(dict(self.parser.items('DATABASE')).values())

        return data

    def get_c_value(self):
        """Reads the values for send_time
        and connection info used to connect to
        RabbitMQ and Flask.
        Returns a list with the values."""

        self.validate_config()

        self.parser.read(strings.get_config_path())

        conn = list(dict(self.parser.items('CONNECTION')).values())

        return conn

    def get_m_keys(self):
        """Reads the keys from the METRICS section.
        Returns a list with the keys."""

        self.validate_config()

        self.parser.read(strings.get_config_path())

        metr = list(dict(self.parser.items('METRICS')).keys())

        return metr

    def get_d_keys(self):
        """Reads the keys from DATABASE section.
        Returns a list with the keys."""

        self.validate_config()

        self.parser.read(strings.get_config_path())

        data = list(dict(self.parser.items('DATABASE')).keys())

        return data

    def get_c_keys(self):
        """Reads the keys for the CONNECTION section.
        Returns a list with the keys."""

        self.validate_config()

        self.parser.read(strings.get_config_path())

        conn = list(dict(self.parser.items('CONNECTION')).keys())

        return conn
