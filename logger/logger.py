import functools
import logging
import logging.config

import yaml


def load_logging_config(config_file: str = 'config/config.yml'):
    """ Loads logging config from an yaml file
    """
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)


# LoggerFactory to load logger configuration file
class LoggerFactory:
    """
    LoggerFactory class.
    """

    def __init__(self, config_file='config.yaml'):
        """
        Initialize the LoggerFactory class. loads the logging configuration from yaml file. Need to have config.yaml
        in the directory
        """
        self.config_file = config_file
        load_logging_config(config_file)


# Decorator to load yaml based config
def log(config_file: str = 'config/config.yml'):
    """ function that returns the decorator
    """

    def decorator(func):
        """ Decorator to load logging config from yaml file
        """

        @functools.wraps(func)
        def log_wrapper(*args, **kwargs):
            """ Wraps the function to load the logging config from config.yaml and
                log the function name and arguments
            """
            load_logging_config(config_file)
            logging.info(
                f"{func.__name__} called with args: {args} and kwargs: {kwargs}")
            return func(*args, **kwargs)

        return log_wrapper

    return decorator
