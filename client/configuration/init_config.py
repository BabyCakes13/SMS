"""Calls the creation and verification of the configuration file and ID file"""
from client.configuration import create_config
from client.configuration import create_id


def initialise_configuration_id():
    """Initialises the configuration file and ID file."""

    create_config.Configuration()
    id_handler = create_id.UniqueID()
    id_handler.setup_id_file()
