"""Module which creates config.ini file."""
import configparser
from client.files import strings
from client.configuration import validator


class Config:
    """Class which handles the creation
    and validity of configuration file."""

    def __init__(self):
        """Initialises the config parser to create
        the config.ini file."""

        self.config = configparser.ConfigParser()
        self.validator = validator.Validator()

        if self.validator.check_config() is False:
            self.set_config()

    def set_config(self):
        """Creates and writes the config.ini file."""

        self.config['CONNECTION'] = strings.get_config_connection()
        self.config['DATABASE'] = strings.get_config_db()
        self.config['METRICS'] = strings.get_config_metrics()

        with open(strings.get_config_path(), 'w') as file:
            self.config.write(file)
