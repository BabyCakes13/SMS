"""Module which tests the methods from create_unique_id module."""
import unittest
import os
import re
from client.configuration import create_id
from client.files import strings


class TestCreateId(unittest.TestCase):
    """Tests the methods from the create_unique_id module."""

    @classmethod
    def setUpClass(cls):
        """Initialises the class variables and ID handler."""

        cls.root_path = os.path.dirname(os.path.abspath(__file__))[:-24]
        cls.id_path = os.path.join(cls.root_path, "files\\id.txt")
        print(cls.id_path)
        cls.id_handler = create_id.UniqueID()

    def test_validate_id_file(self):
        """Tests whether the ID file is correctly validated."""
        with open(self.id_path, "w+") as f_id:
            f_id.write("this is such a bad thing to do.")

        with open(self.id_path, "r") as f_id:
            self.assertFalse(re.search(strings.get_id_re(), f_id.read()))

        self.id_handler.setup_id_file()

        with open(self.id_path, "r") as f_id:
            self.assertTrue(re.search(strings.get_id_re(), f_id.read()))

    def test_setup_id_file(self):
        """Tests if the setup_id_file method works correctly.
        It should create a file if it doesn't exist or
        has an incorrect structure."""

        self.id_handler.setup_id_file()
        os.remove(self.id_path)
        self.assertFalse(os.path.isfile(self.id_path))

        self.id_handler.setup_id_file()
        self.assertTrue(os.path.isfile(self.id_path))

    def test_check_id(self):
        """Tests if the check_id method returns the right answer."""

        os.remove(self.id_path)
        is_file = os.path.isfile(self.id_path)
        is_valid = self.id_handler.validate_id_file()

        self.assertFalse(is_file and is_valid)

        self.id_handler.setup_id_file()
        is_file = os.path.isfile(self.id_path)
        is_valid = self.id_handler.validate_id_file()

        self.assertTrue(is_file and is_valid)

        self.id_handler.setup_id_file()
        with open(self.id_path, "w") as f_id:
            f_id.write("this is for sure not valid.")
        is_file = os.path.isfile(self.id_path)
        is_valid = self.id_handler.validate_id_file()

        self.assertFalse(is_file and is_valid)
