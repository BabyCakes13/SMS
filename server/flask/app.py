"""Module which uses Flask to get the packets out of the database
and make them available to web use."""
import flask
import packets
from util import identifier, configurator, reader
from server.threads import get_rpack, db_handler

APP = flask.Flask(__name__, template_folder="templates")
CONFIG = configurator.Config()
READER = reader.Reader()
DATABASE_HANDLER = db_handler.Database(APP)


@APP.route('/')
def main_page_route():
    """Displays the main page and the types of information
     you can get the server to display."""

    return flask.render_template("main_page.html")


@APP.route('/current_supported_metrics')
def current_supported_metrics_route():
    """Displays the currently supported metrics."""

    return flask.render_template("current_supported_metrics.html",
                           metrics=READER.get_m_keys())


@APP.route('/packets')
def packets_route():
    """Displays information about all the packages in the database."""

    all_packets = DATABASE_HANDLER.get_all()
    packets_list = []

    for packets in all_packets:
        for packet in packets:
            del packet['_id']
            packets_list.append(packet)

    return flask.render_template("all_packets.html", packets=packets_list)


@APP.route('/packets/<packet_id>')
def packets_id_route(packet_id):
    """Displays information about a package based on the package ID"""
    packet_info = DATABASE_HANDLER.get_pack(str(packet_id))

    for packet in packet_info:
        packets_new = DATABASE_HANDLER.delete_dbid(packet)

    return flask.render_template("packet_information.html", packets=packets_new)


@APP.route('/metrics', methods=['GET'])
def packets_metrics_route():
    """Gets the requested metrics and show only
     that information for all nodes."""
    metrics = flask.request.args.to_dict().values()
    node_info_list = []

    if check_metric(metrics) is True:

        cursor_list = DATABASE_HANDLER.get_all()

        for cursor in cursor_list:
            for cursor_item in cursor:

                temp_dict = {
                    "ID": cursor_item.get('ID'),
                }

                for metric in metrics:
                    temp_dict[metric] = cursor_item.get('%s' % metric)

                node_info_list.append(temp_dict)

    return flask.render_template("packet_information.html", packets=node_info_list)


def check_metric(metrics):
    """Checks whether the argument is part
    of the current supported metric list."""

    for metric in metrics:
        is_supported = False
        for supported in READER.get_m_keys():
            if str(supported) == str(metric):
                is_supported = True

    return is_supported


if __name__ == '__main__':

    CONSUME_PACKET = get_rpack.RabbitObjectHandler(APP)
    CONSUME_PACKET.start()

    configurator.Config()
    identifier.Identifier()
    pack = packets.Packet()
    pack.start_sending(pack.connection)

    APP.run(READER.get_c_value()[1], READER.get_c_value()[3])


