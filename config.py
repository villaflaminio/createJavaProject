import configparser
import os

configApp = configparser.ConfigParser()
configApp.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini'))

# PATH
PATH_DIR = os.environ.get("PATH_DIR") or configApp['PATH']['PATH_DIR']
PATH_LOG = os.environ.get("PATH_LOG") or configApp['PATH']['PATH_LOG']



