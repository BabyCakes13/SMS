"""Contains the tests for the create_configuration module"""
import unittest
import os
from client.configuration import create_config
from client.files import strings


class TestCreateConfigurationFile(unittest.TestCase):
    """Test which verifies if the configuration
    file is correctly created and verified."""

    @classmethod
    def setUpClass(cls):

        cls.root_path = os.path.dirname(os.path.abspath(__file__))[:-24]
        cls.config_path = os.path.join(cls.root_path, "files\\parser.txt")

        cls.test = create_config.Configuration()

    def test_validate_structure(self):
        """Tests if the validate_structure() function
        the file structure is correctly handled."""

        with open(self.config_path, "w") as f_config:
            f_config.write(strings.get_configuration_file_form())

        self.assertEqual(self.test.validate_configuration_file(), True)

        with open(self.config_path, "w") as f_config:
            f_config.write("This will be bad.")

        self.assertEqual(self.test.validate_configuration_file(), False)

    def test_check_configuration(self):
        """Tests if the initialise_configuration_id() function creates,
        verifies and writes the file correctly."""

        self.test.check_configuration()
        self.assertEqual(os.path.isfile(self.config_path), 1)

        f_config = open(self.config_path, "r+")
        self.assertEqual(f_config.read(), strings.get_configuration_file_form())

        f_config.close()
