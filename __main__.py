"""Module which starts the application. It starts the Flask server,
and after validating the configuration and id.txt, it starts
sending packets to RabbitMQ, and consuming them in the database."""
from client import packets, start_sending
from server import start_consuming
from server.flask import app
from util import configurator, identifier, reader


def start_threads(connection, flask_app, packet_id):
    """Stats the thread which sens metrics to the RabbitMQ queue
    and the thread which consumes it and adds it to the database."""

    while True and connection is not None:

        try:
            client = start_sending.PacketThread(connection,
                                                packet_id)
            server = start_consuming.RabbitThread(flask_app)

            client.daemon = True
            server.daemon = True

            client.start()
            server.start()

        except(KeyboardInterrupt, SystemExit):
            print("Stopped connection.")
            exit(0)


def start():
    """It first validates the config.ini file.
       It sets connection to the RabbitMQ queue to send the metrics.
       Sets the machine id.
       It starts the Flask server, then the client and server thread
       on send and consume side of RabbitMQ."""

    configurator.Config()
    identifier.Identifier()
    reader.Reader()

    metrics = packets.Packet()
    machine_id = metrics.machine_id

    rabbit_connection = metrics.set_connection()

    app.start_app()

    start_threads(rabbit_connection, app.APP, machine_id)


if __name__ == '__main__':

    start()
