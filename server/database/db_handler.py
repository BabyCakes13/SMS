"""Module which manages the information sent by the Flask server."""
from flask_pymongo import PyMongo
from config_util import reader


class DatabaseHandler:
    """Enables adding an object of the type metrics, time and id to the database,
    configuring the database with user and ur,
     get information about the data."""

    def __init__(self, app):
        """Configures the mongodb name and uri
        using the reader in client."""

        self.app = app

        read = reader.Reader()

        self.app.config['MONGODB_NAME'] = read.get_d_value()[0]
        self.app.config['MONGO_URI'] = read.get_d_value()[1]

    def add_packet_to_database(self, packet):
        """Adds a packet to the database."""

        database = PyMongo(self.app)
        inserter = database.db.node
        inserter.insert(packet)

    def get_packet_info(self, packet_id):
        """Searches for the data of a specific node,
         given by the IP address."""

        database = PyMongo(self.app)
        inserter = database.db.node

        packets = inserter.find({'ID': packet_id})

        return packets

    def get_all_packets(self):
        """Returns all packets"""
        database = PyMongo(self.app)
        packet_id_list = database.db.node.distinct('ID')
        packet_info_list = []

        for ids in packet_id_list:
            packet_info_list.append(
                database.db.node.find({'ID': ids}).limit(1))

        return packet_info_list

    @classmethod
    def delete_database_id(cls, packet):
        """Deletes he database id"""

        new_packet = packet
        del new_packet['_id']
        return new_packet
