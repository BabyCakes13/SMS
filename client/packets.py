"""Module which handles the creation and transmission of packets.
Packets are formed of metric values
collected from the PC, sent based on
the send_time set in config.txt file,
the unique id, representing the machine
on which the program is currently run, and the
time at which each packet was sent."""
import rabbitmq
from util import identifier, reader


class Packet:
    """Handles the sending of the packets formed from
    metric values and id to the rabbit mq server,
    based on the configured send time."""

    def __init__(self):
        """Creates the dictionary containing the collected packet,
        unique id and the time when the object was sent.
        Uses the given port and address to connect to the rabbit queue
        and sends the packet dictionary."""

        self.reader = reader.Reader()
        id_handler = identifier.Identifier()
        self.machine_id = id_handler.get_id()

        self.connection = self.set_connection()

    def set_connection(self):
        """Initialises the connection to the RabbitMQ queue.
        Starts the thread to send packets to the queue."""

        rabbit_connection = False
        address = self.reader.get_c_value()[1]
        port = self.reader.get_c_value()[2]

        try:
            rabbit_connection = \
                rabbitmq.RabbitMQ(address, port)
        except(AttributeError, ConnectionError):
            print("Connection error to RabbitMQ.")

        return rabbit_connection
