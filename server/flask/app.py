"""Module which uses Flask to get the packets out of the database
and make them available to web use."""
import flask
from util import configurator
from util import reader
from server import database, flask_server

APP = flask.Flask(__name__, template_folder="templates")
CONFIG = configurator.Config()
READ = reader.Reader()
DATABASE = database.Database(APP)


def start_app():
    """Starts the thread which runs Flask APP."""

    thread = flask_server.FlaskThread(APP)
    thread.setDaemon(True)
    thread.start()


@APP.route('/')
def main_page_route():
    """Displays the main page and the types of information
     you can get the server to display."""

    return flask.render_template("main_page.html")


@APP.route('/supported_metrics')
def supported_metrics_route():
    """Displays the currently supported metrics."""

    return flask.render_template("supported_metrics.html",
                                 metrics=READ.get_m_keys())


@APP.route('/packets')
def packets_route():
    """Displays information about all the packages in the database."""

    all_packets = DATABASE.get_all()
    packets = []

    for packet in all_packets:
        for pack in packet:
            del pack['_id']
            packets.append(pack)

    return flask.render_template("all_packets.html", packets=packets)


@APP.route('/packets/<packet_id>')
def packets_id_route(packet_id):
    """Displays information about a package based on the package ID"""

    packet_info = DATABASE.get_pack(str(packet_id))

    for packet in packet_info:
        packets = DATABASE.delete_dbid(packet)

    return flask.render_template("packet_information.html", packets=packets)


@APP.route('/metrics', methods=['GET'])
def metrics_route():
    """Gets the requested metrics and show only
     that information for all nodes."""

    metrics = flask.request.args.to_dict().values()
    packets = []

    if check_metric(metrics) is True:

        cursor_list = DATABASE.get_all()

        for cursors in cursor_list:
            for cursor in cursors:

                info = {
                    "ID": cursor.get('ID'),
                }

                for metric in metrics:
                    info[metric] = cursor.get('%s' % metric)

                packets.append(info)

    return flask.render_template("packet_information.html", packets=packets)


def check_metric(metrics):
    """Checks whether the argument is part
    of the current supported metric list."""

    for metric in metrics:
        is_supported = False
        for supported in READ.get_m_keys():
            if str(supported) == str(metric):
                is_supported = True

    return is_supported
