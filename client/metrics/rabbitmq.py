"""Module which handles the RabbitMQ connection,
packets sending and queue handling."""
import pika


class RabbitConnection:
    """Handles the connection to the RabbitMQ server,
    transmission of packets and closing the channel."""

    def __init__(self, address, port):
        """Creates a connection to the RabbitMQ server
        using the given port and address and
        opens a queue in which the metrics will
        be stored for the server to take."""

        connection = \
            pika.BlockingConnection(pika.ConnectionParameters(address, port))
        self.rabbit_connection = connection.channel()
        self.rabbit_connection.queue_declare(queue='metrics_queue')

    def send_packet(self, packet):
        """Sends given packets to the RabbitMQ queue"""

        self.rabbit_connection.basic_publish(exchange='',
                                             routing_key='metrics_queue',
                                             body=packet)

        print("sent..." + packet)

    def stop_connection(self):
        """Stops the connection to the RabbitMQ server."""

        print("connection to RabbitMQ closed...")
        self.rabbit_connection.close()
