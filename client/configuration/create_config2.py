import sys
from client.files import strings


class Config(object):
    """Class which handles the creation
    and validity of configuration file."""

    def __init__(self):

        self.config_path = sys.argv[0]
        print(self.config_path)
