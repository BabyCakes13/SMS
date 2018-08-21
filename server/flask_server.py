"""Module which hold the class with the Flask server thread"""
import threading
from util import reader


class FlaskThread(threading.Thread):
    """Class which holds the thread to run the Flask server."""

    def __init__(self, app):
        """Starts the thread which runs the Flask server."""

        self.app = app
        threading.Thread.__init__(self)

        thread = threading.Thread(target=self.run_app)
        thread.setDaemon(True)
        thread.start()

    def run_app(self):
        """Starts the flask server."""

        read = reader.Reader()
        self.app.run(read.get_c_value()[1],
                     read.get_c_value()[3])
