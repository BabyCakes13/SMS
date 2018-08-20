import time
from client import packets, client_thread
from server.flask import app
from server import server_thread
from util import configurator, identifier, reader
from server import flask_thread


def start_threads(connection, app, machine_id, sleep):
    """Stats the thread which sens metrics to the RabbitMQ queue
    and the thread which consumes it and adds it to the database."""

    while True and connection is not None:

        try:
            client = client_thread.PacketThread(connection,
                                                machine_id)
            server = server_thread.RabbitThread(app)

            client.daemon = True
            server.daemon = True

            client.start()
            server.start()

        except(KeyboardInterrupt, SystemExit):
            print("Stopped connection.")
            exit(0)


if __name__ == '__main__':

    configurator.Config()
    identifier.Identifier()
    read = reader.Reader()

    send_metric = packets.Packet()
    rabbit_connection = send_metric.set_connection()

    machine_id = send_metric.machine_id
    sleep = int(read.get_c_value()[0])
    app = app.get_app()

    flask = flask_thread.FlaskThread()
    flask.daemon = True
    flask.start()

    start_threads(rabbit_connection, app, machine_id, sleep)

    print("started!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    #app.APP.run(read.get_c_value()[1], read.get_c_value()[3], threaded=True)
