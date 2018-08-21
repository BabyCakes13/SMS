"""Module which contains the thread which sends
the metric packets to the server."""
import json
import threading
import time
import metrics
from util import reader, strings


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

        send_time = int(self.r_handler.get_c_value()[0])
        time.sleep(send_time)

    def run(self):
        """Sends the packets with data to the RabbitMQ queue."""

        self.packet['time'] = strings.get_time()
        self.packet.update(self.m_handler.get_values())

        self.rabbit_connection.send_packet(json.dumps(self.packet, indent=1))
