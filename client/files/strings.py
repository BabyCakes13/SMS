"""Module which contains strings used in the project"""
import os


def get_config_path():
    """Contains the path to the configuration
    file, parser.ini."""

    root = os.path.dirname(os.path.abspath(__file__))[:-13]
    config = os.path.join(root, 'config2.ini')

    return config


def get_config_metrics():
    """Contains the configuration file form
    for the metrics and metrics default values."""

    metrics = {'disk_usage': 'YES',
               'cpu_percent': 'YES',
               'memory_info': 'YES',
               'cpu_stats': 'YES'}

    return metrics


def get_config_db():

    db = {'db_name': 'database_name',
          'db_url': 'database_url'}

    return db


def get_config_connection():

    connection = {'send_time': '5',
                  'address': 'localhost',
                  'port': '5672',
                  'flask_port': '500'}

    return connection


def get_values_re():
    """Contains the regex expressions
    for the values for sections CONNECTION
    and METRICS."""

    re = r"([1-9]|1[0-9]) " +\
         r"(localhost) " +\
         r"(\d{1,5}) " +\
         r"(\d{1,5}) " +\
         r"(YES|NO) " +\
         r"(YES|NO) " +\
         r"(YES|NO) " + \
         r"(YES|NO)"

    re = re.split(" ")

    return re


def get_configuration_file_form():
    """Contains the structure of the configuration
    file used by the client to choose the metrics"""

    return "DISK_USAGE=TRUE" \
        "\nCPU_PERCENT=TRUE" \
        "\nMEMORY_INFO=TRUE" \
        "\nCPU_STATS=TRUE" \
        "\nSEND_TIME=5" \
        "\nADDRESS=localhost" \
        "\nPORT=5672"


def get_configuration_file_re():
    """Contain the regex expression to check
    the validity of the configuration file"""

    return r"DISK_USAGE=(TRUE|FALSE)" \
        r"\nCPU_PERCENT=(TRUE|FALSE)" \
        r"\nMEMORY_INFO=(TRUE|FALSE)" \
        r"\nCPU_STATS=(TRUE|FALSE)" \
        r"\nSEND_TIME=([1-9]|1[0-9])" \
        r"\nADDRESS=(localhost)" \
        r"\nPORT=(\d{1,5})"


def get_metrics_re():
    """Contains the regex expression to check the validity of
    only the metrics from the configuration file"""

    return r"DISK_USAGE=(TRUE|FALSE)" \
        r"\nCPU_PERCENT=(TRUE|FALSE)" \
        r"\nMEMORY_INFO=(TRUE|FALSE)" \
        r"\nCPU_STATS=(TRUE|FALSE)"


def get_send_time_re():
    """Contains the regex expression for the type of communication time."""

    return r"SEND_TIME=[1-9][0-9]|[1-9]"


def get_port_re():
    """Contains the regex for the port type."""

    return r"PORT=(\d{1,5})"


def get_address_re():
    """Contains the regex for address type."""

    return r"ADDRESS=localhost"


def get_sent_time_format():
    """Contains the format for sent time of packet."""

    return "%Y-%m-%d %H:%M:%S"


def get_data_names():
    """Contains the metric, id and sent time names."""

    metric_names = \
        ['Disk_Usage', 'Cpu_Percent', 'Memory_Info', 'Cpu_Stats', 'ID', 'Time']

    return metric_names


def get_id_re():
    """Returns the regex expression for the id form."""

    return r"[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}"
