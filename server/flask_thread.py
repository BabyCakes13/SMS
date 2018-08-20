import threading
import flask
from server import db_handler
from util import reader


class FlaskThread(threading.Thread):

    APP = flask.Flask(__name__, template_folder="server.flask.templates")

    def __init__(self):

        threading.Thread.__init__(self)

        self.READER = reader.Reader()
        self.DATABASE_HANDLER = db_handler.Database(self.APP)

    def run(self):

        self.APP.run(self.READER.get_c_value()[1], self.READER.get_c_value()[3])

    @staticmethod
    @APP.route('/')
    def main_page_route():
        """Displays the main page and the types of information
         you can get the server to display."""

        return "hello"
