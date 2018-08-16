"""Module which contains strings used in the project"""


def get_config_metrics():
    """Contains the configuration file form
    for the metrics and metrics default values."""

    metrics = ['DISK_USAGE',
               'CPU_PERCENT',
               'MEMORY_INFO',
               'CPU_STATS']

    default = ['TRUE',
               'TRUE',
               'TRUE',
               'TRUE']

    return metrics, default


def get_config_settings():

    settings = ['SEND_TIME',
                'ADDRESS',
                'PORT']

    default = ['5',
               'localhost',
               '5672']

    return settings, default


def get_configuration_file_form():
    """Contains the structure of the configuration
    file used by the client to choose the metrics"""

    return "DISK_USAGE=TRUE" \
        "\nCPU_PERCENT=TRUE" \
        "\nMEMORY_INFO=TRUE" \
        "\nCPU_STATS=TRUE" \
        "\nSEND_TIME=2" \
        "\nADDRESS=localhost" \
        "\nPORT=5672"


def get_configuration_file_re():
    """Contain the regex expression to check
    the validity of the configuration file"""

    return r"DISK_USAGE=(TRUE|FALSE)" \
        r"\nCPU_PERCENT=(TRUE|FALSE)" \
        r"\nMEMORY_INFO=(TRUE|FALSE)" \
        r"\nCPU_STATS=(TRUE|FALSE)" \
        r"\nSEND_TIME=([1-9]|[1-9][0-9])" \
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
