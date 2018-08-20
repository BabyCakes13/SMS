"""Module which takes the packets from the RabbitMQ and
stores them in the database."""
import json
from threading import Thread
import pika
from util.strings import get_rabbit_queue
from util import reader
from server.threads import db_handler


class RabbitObjectHandler(Thread):
    """Class which handles the packets fromm the RabbitMQ queue."""

    def __init__(self, app):
        """Initialises the connection between RabbitMQ queue and Flask server,
        in order to get the objects waiting in Rabbit queue and put them in
        the database."""

        Thread.__init__(self)

        self.connection = False
        self.app = app

        self.connect()
        self.database = db_handler.Database(self.app)

    def connect(self):
        """Connects to the RabbitMQ queue."""

        read = reader.Reader()

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                read.get_c_value()[1], read.get_c_value()[2]))
        self.connection = connection.channel()
        self.connection.queue_declare(queue=get_rabbit_queue())

    def collect_packet(self, channel, method, properties, body):
        """Adds the packet collected from the RabbitMQ
         queue to the database."""

        self.database.add_pack(json.loads(body))
        print("added...")
        print(body)

    def run(self):
        """Starts the thread which consumes the objects
         from the RabbitMQ queue."""

        self.connection.basic_consume(self.collect_packet,
                                      queue=get_rabbit_queue(),
                                      no_ack=True)

        self.connection.start_consuming()
