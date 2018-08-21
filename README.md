# SMS

------------------------------------------------------
DESCRIPTION
------------------------------------------------------
 
The project collects metric information from the client PC and sends them to a RabbitMQ queue.
The packets will be then stroed in a MongoDb database and with Flask, displayed in html format.
The project is formed of two parts: client and server.

------------------------------------------------------
CLIENT
------------------------------------------------------

FILES:

id.txt:

This is the machine ID generated to uniquely identify the machine the application is running on.
This is used in the packets send by the client to the server.
Using this ID, one can identify the other packets the same machine sent.

metrics.py:

This module is used to read the config.ini file to get the metrics which were opted as YES, and calls the 
functions for each wanted metric.

packets.py:

This module sets the machine id for a packet and starts the connection to RabbitMQ queue.
The name of the queue can be changed in util.strings.get_queue_name().
It connects to the address and port specified in the config.ini file.

rabbitmq.py:

This module connects to the RabbitMQ queue and handles sending packets to it.


start_sending.py:

This module contains the thread which sends packets to the RabbitMQ queue.
One packet is created of the results from the desired metrics, the unique machine ID and the time 
the packet was sent.

------------------------------------------------------
SERVER
------------------------------------------------------

FILES:

app.py:

This module establishes the routes which display packet information.
Instructions using the information is displayed on the main page.
The Flask server is sent to the database object which is used to gather
information collected from the RabbitMQ queue.

database.py:

This module configures the connectionn between the MongoDB database where the metric
information is stored and the Flask server to display that information. 
The database URI and name must be specified in the config.ini file before running the program.

flask_server.py:

This module contains the thread which runs the Flask server.
It connects to the address and flask_port found in config.ini.

start_consuming.py:

This module starts the thread which consumes the packets from the RabbitMQ queue, and adds
them to the database.

OTHER FILES:

------------------------------------------------------
UTIL
------------------------------------------------------

FILES:

configurator.py:

This module handles the config.ini file. It checks whether the file is valid and exists. 
In case this doesn't happen, it creates a new default one. 

identifier.py:

This module handles the creation of the unique machine identifier.
It send the ID with the metrics in each packet, so each packet can be
associated with a machine, ensuring that the identifier is unique.

reader.py:

This module handles reading information from the config.ini file.

strings.py:

This module contains the strings used in the project.
The rabbitmq queue name can be changed here, also default
config.ini file.

validator.py:

This module handles validating the config.ini file. It checks that the structure is
correct and that the options are valid.

------------------------------------------------------
ROOT FILES
------------------------------------------------------

.gitignore: 

This file contains modules which will be ignored by git.

__main__.py:

This module is the starting point of the application.
It calls the three threads: sending, collecting and running the Flask server.

config.ini:

This file is used by the client to specify which metrics to be collected, connection info and database info.
The client must setup a mLab MongoDB database, and replace the db_url with the generated uri and db_name
with the chosed database name.
Send_time represents how many seconds will pass between each collection of metrics and sending.
If the user wants to collect metrics every 10 seconds, replace send_time = 10.
The user can chose which metrics to be sent by changing YES/NO in config.ini file.
If disk_usage = NO, then this metric will not be collected/sent.

------------------------------------------------------
INSTRUCTIONS
------------------------------------------------------

First, create a database using mLab MongoDB database.
In order to run the project, the config.ini file must be completed.
CONNECTION - setup connection information
- send_time: choose an interval at which metrics will be send.
- address: for now localhost on which the project will be run.
- port: the port on which the RabbitMQ will connect.
- flask_port: the port on which the Flask server will run.

DATABASE:

- db_name: after creating the database, complete the name of the database here
- db_url: after creating the database, complete the generated uri of the database.

METRICS:

change YES to NO if you don't want the specific metric to be collected.

After completing the config.ini file, run  __main__py in order to start the application.
Then go to the generated link. Example: https://localhost:500

PAGES:

https://localhost:500 - this is the main page. Instructions on using the other pages are found here.
https://localhost:500/supported_metrics - this displays the current supported metrics which can be collected
https://localhost:500/packets - this displays all the packets from distinct machines. (different ID). 
                              last collect is showed for each machine.
https://localhost:500/packets/"id" - using the ID of one packet, show information only for that packet
https://localhost:500/metrics/"variables" - choose which metrics to be shown for the packets.
