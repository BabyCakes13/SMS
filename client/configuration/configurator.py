"""Module which creates parser.ini file."""
import configparser
from client.files import strings
from client.configuration import validator


class Config:
    """Class which handles the creation
    and validity of configuration file."""

    def __init__(self):
        """Initialises the parser parser to create
        the parser.ini file."""

        self.parser = configparser.ConfigParser()
        self.validator = validator.Validator()

        self.set_requirements()

        if self.validator.check_config() is False:
            self.set_config()

    @staticmethod
    def set_requirements():
        """Creates the requirements file in case
        is has been altered or deleted."""

        with open(strings.get_requirements_path(), "w")  as file:
            file.write(strings.get_requirements())

    def set_config(self):
        """Creates and writes the parser.ini file."""

        self.parser['CONNECTION'] = strings.get_config_connection()
        self.parser['DATABASE'] = strings.get_config_db()
        self.parser['METRICS'] = strings.get_config_metrics()

        with open(strings.get_config_path(), 'w') as file:
            self.parser.write(file)
