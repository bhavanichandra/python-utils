import logging
import pathlib

from logger.logger import LoggerFactory

BASE_DIR = pathlib.Path(__file__).parent.resolve()
config_file = BASE_DIR / 'config.yaml'

LoggerFactory(config_file=config_file)

logging.info('Starting multithreading')
