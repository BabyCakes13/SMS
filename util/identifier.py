"""Module which contains the Identifier class to
handler the unique identifier of a machine running
the program."""
import subprocess
from util import strings


class Identifier:
    """Class which configures the unique id of the machine.
    It uses UUID from wmic csproduct to get an unique code
    for the machine the program is running on, in order to
    identity the machine which sent the packets to the server."""

    def __init__(self):
        """Calls check_id to verify if changed needed to be done
        to id.txt file. If the file is corrupt, it creates another."""

        if self.validate_id() is False:
            self.set_id()

    def set_id(self):
        """Creates the id.txt file which contains the
        UUID of the machine."""

        with open(strings.get_id_path(), "w+") as file:
            file.write(self.get_uuid())

    def validate_id(self):
        """Checks if id.txt exists and if the id found
         in id.txt is the correct id."""

        try:
            file = open(strings.get_id_path(), "r")
        except IOError:
            return False

        correct_id = self.get_uuid()
        read_id = file.read()

        file.close()

        return correct_id == read_id

    def get_id(self):
        """Returns the UUID found in id.txt file."""

        if self.validate_id() is False:
            self.set_id()

        with open(strings.get_id_path(), "r") as file:
            return file.read()

    @staticmethod
    def get_uuid():
        """Gets the UUID from the Windows to uniquely identity
        the machine."""

        uuid = subprocess.check_output('wmic csproduct get UUID',
                                       universal_newlines=True)
        uuid = uuid.split()[1]

        return uuid
