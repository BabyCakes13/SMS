"""Module which creates the ID.txt file if it does not exist
or it's invalid."""
import os
import re
import uuid
from client.files import strings


class UniqueID:
    """Class which handles the creation and validity of
    the ID file."""

    def __init__(self):
        """Keeps the path to the id.txt file in id_path.
        If the id.txt file already exists and it's valid,
        then it does nothing.
        Else, it creates a new ID file."""

        self.root_path = os.path.dirname(os.path.abspath(__file__))[:-14]
        self.id_path = os.path.join(self.root_path, "files\\id.txt")

        if self.check_id() is False:
            self.setup_id_file()

    def setup_id_file(self):
        """Creates the id.txt file, which contains the ID for one machine.
        In case the ID is altered, another one is created."""

        with open(self.id_path, "w+") as f_id:

            f_id.write(str(UniqueID.create_id()))

    def validate_id_file(self):
        """Checks whether the structure of the ID file is correct."""

        try:
            f_id = open(self.id_path, "r")
        except IOError:
            return False

        is_valid = bool(re.search(strings.get_id_re(), f_id.read()))

        f_id.close()

        return is_valid

    def check_id(self):
        """Checks if the id.txt file exists and is valid.
        If false, it creates another ID."""

        is_file = os.path.isfile(self.id_path)
        is_valid = self.validate_id_file()
        return bool(is_file and is_valid)

    def read_id(self):
        """Returns the ID read form the id.txt file."""
        with open(self.id_path, "r") as f_id:
            return f_id.read()

    @staticmethod
    def create_id():
        """Creates an unique ID of the form {8}_{4}_{4}_{12}"""
        return uuid.uuid4()
