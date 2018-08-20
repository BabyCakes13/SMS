"""Setup file of the client side of the project."""

from setuptools import find_packages
from setuptools import setup

setup(name='SMS',
      version='0.1',
      description='Application which collects metrics from'
                  'PC and displays them to localhost.',
      url='https://github.com/BabyCakes13/SMS.git',
      author='Maria Minerva Vonica',
      author_email='maria.vonica98@gmail.com',
      install_requires=['flask',
                        'flask_pymongo',
                        'pika',
                        'psutil',
                        'pymongo',
                        ],
      packages=find_packages()
      )
