"""Module which handles the creation and transmission of packets.
Packets are formed of metric values
collected from the PC, sent based on
the send_time set in config.txt file,
the unique id, representing the machine
on which the program is currently run, and the
time at which each packet was sent."""
import threading
import time
import json
from config_util import identifier, reader
from client.files import strings
from client.packet import metrics, rabbitmq


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

        self.rabbit_connection = False

        self.set_data()

    def set_data(self):
        """Initialises the connection to the RabbitMQ queue.
        Starts the thread to send packets to the queue."""

        address = self.reader.get_c_value()[1]
        port = self.reader.get_c_value()[2]

        try:
            self.rabbit_connection = \
                rabbitmq.RabbitConnection(address, port)
        except(AttributeError, ConnectionError):
            print("Connection error to RabbitMQ.")

        while True:
            try:
                lopper = PacketThread(self.rabbit_connection, self.machine_id)
                lopper.daemon = True
                lopper.start()
                lopper.join()
            except(KeyboardInterrupt, SystemExit):
                print("Stopped connection from keyboard.")
                exit(0)


class PacketThread(threading.Thread):
    """Thread which sends packets to the RabbitMQ queue.
    Data is refreshed based on the set send_time int
    config.ini file. """

    def __init__(self, connection, machine_id):
        """Initialises the thread and packet info which
        will be sent to the RabbitMQ queue."""

        threading.Thread.__init__(self)

        self.r_handler = reader.Reader()
        self.m_handler = metrics.Metric()
        self.rabbit_connection = connection
        self.packet = {'ID': machine_id}

    def run(self):
        """Sends the packets with data to the RabbitMQ queue."""

        self.packet['time'] = strings.get_time()
        self.packet.update(self.m_handler.get_values())

        self.rabbit_connection.send_packet(json.dumps(self.packet, indent=1))

        send_time = int(self.r_handler.get_c_value()[0])
        time.sleep(send_time)
