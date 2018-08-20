"""Module which contains strings used in the project"""
import datetime
import os


def get_config_path():
    """Contains the path to the configuration 
    file, config.ini."""

    root = os.path.dirname(os.path.abspath(__file__))[:-5]
    config_path = os.path.join(root, 'config.ini')

    return config_path


def get_requirements_path():
    """Returns the path to the requirements.txt file."""

    root = os.path.dirname(os.path.abspath(__file__))[:-13]
    req_path = os.path.join(root, 'requirements.txt')

    return req_path


def get_id_path():
    """Returns the path to the id.txt file."""
    
    root = os.path.dirname(os.path.abspath(__file__))[:-5]
    id_path = os.path.join(root, "client\\files\\id.txt")
    
    return id_path


def get_config_metrics():
    """Contains the configuration file form
    for the packet and packet default values."""

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


def get_time():
    """Returns the current time."""

    time_format = "%Y-%m-%d %H:%M:%S"
    now = str(datetime.datetime.now().strftime(time_format))

    return now


def get_rabbit_queue():
    """Contains the name of the rabbitmq queue."""

    return "metrics_queue"