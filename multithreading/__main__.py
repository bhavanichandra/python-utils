import logging

from logger.logger import log

import pathlib

BASE_DIR = pathlib.Path(__file__).parent.resolve()

@log(config_file=BASE_DIR / 'config.yaml')
def test():
    logging.info("test")


