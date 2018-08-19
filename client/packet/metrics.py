"""Module which contains the class which handles
system metrics."""
import os
import psutil
from config_util import reader


class Metric:
    """Class which contains methods to gather system
    information from the PC."""

    def __init__(self):
        """Initialises a reader to read the config.ini file."""

        self.reader = reader.Reader()

    def get_values(self):
        """Returns the values of the selected
        metrics from the current PC."""

        m_values = self.reader.get_m_value()
        m_names = self.reader.get_m_keys()
        sys_data = {}

        for i, metric in enumerate(m_names):
            method_name = 'get_%s' % metric
            if hasattr(self, method_name) and m_values[i] == 'YES':
                sys_data[metric] = getattr(self, method_name)()

        return sys_data

    @staticmethod
    def get_disk_usage():
        """Returns the disk usage."""
        return psutil.disk_usage(os.path.abspath(os.sep))

    @staticmethod
    def get_cpu_percent():
        """Returns the cpu percent."""
        return psutil.cpu_percent(interval=1, percpu=True)

    @staticmethod
    def get_memory_info():
        """Returns the memory info."""
        return psutil.virtual_memory()

    @staticmethod
    def get_cpu_stats():
        """Returns the cpu_stats."""
        return psutil.cpu_stats()
