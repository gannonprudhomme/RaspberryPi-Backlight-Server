import sys
import logging

def setup_logging():
    """ Sets up logging for the project """
    logging.basicConfig(format='%(levelname)s %(asctime)s: %(message)s',
                        datefmt='%I:%M:%S %p',
                        handlers=[ # Log to both a file and stdout
                            logging.FileHandler('logs.log'),
                            logging.StreamHandler(sys.stdout)
                        ], level=logging.INFO)
