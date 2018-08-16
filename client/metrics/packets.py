"""Module which handles the creation and transmission of packets.
Packets are formed of metric values collected from the PC, changing based on
the send time set in config.txt file, the unique id representing the machine
and the time at which each packet was sent."""
import json
import threading
import datetime
import time
from client.files import strings
from client.metrics import rabbitmq, get_metrics
from client.configuration import read_config, create_id


class PacketHandler:
    """Handles the sending of the packets formed from
    metric values and id to the rabbit mq server,
    based on the configured send time."""

    def __init__(self):
        """Creates the dictionary containing the collected metrics,
        unique id and the time when the object was sent.
        Uses the given port and address to connect to the rabbit queue
        and sends the metrics dictionary."""

        self.reader = read_config.ReaderHandler()
        self.rabbit_connection = False
        self.address = self.reader.get_address()
        self.port = self.reader.get_port()

    def set_packet_data(self):
        """Stores data which is not changing in the class attributes.
        Adds the id of the machine to the sent packet."""

        try:
            self.rabbit_connection = \
                rabbitmq.RabbitConnection(address=self.address, port=self.port)
        except(AttributeError, ConnectionError):
            print("Connection Error.")

        while True:
            try:
                lopper = PacketThread(self.rabbit_connection)
                lopper.daemon = True
                lopper.start()
                lopper.join()
            except(KeyboardInterrupt, SystemExit):
                print("stopped connection from keyboard...")
                exit(0)


class PacketThread(threading.Thread):
    """Thread which sends packets to the RabbitMQ queue.
    It sleeps for the given send_time set in config.ini."""

    def __init__(self, connection):
        """Initialises the thread and packet info which
        will be sent to the RabbitMQ queue."""

        threading.Thread.__init__(self)

        self.reader = read_config.ReaderHandler()
        self.rabbit_connection = connection
        self.packet = {}

        unique_id = create_id.UniqueID()
        self.packet[strings.get_data_names()[4]] = str(unique_id.read_id())

    def run(self):
        """Sends the packets with info to the RabbitMQ queue."""

        metrics = get_metrics.Metrics()
        now = str(datetime.datetime.now().strftime(strings.get_sent_time_format()))

        self.packet[strings.get_data_names()[5]] = now
        self.packet.update(metrics.get_metrics_values())

        self.rabbit_connection.send_packet(json.dumps(self.packet, indent=1))

        time.sleep(int(self.reader.get_send_time()))

