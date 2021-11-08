import threading
import logging
import sys



from logger.logger import log

@log
def test():
    logging.info("test")
