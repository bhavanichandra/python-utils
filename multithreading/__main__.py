from logger.logger import log

import logging
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.resolve()
config_file = BASE_DIR / 'config.yaml'


@log(config_file=config_file.__str__())
def test():
    logging.info("test")


test()