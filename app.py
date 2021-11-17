import logging
import pathlib
import sys
import time
from concurrent.futures import ThreadPoolExecutor

from logger.logger import LoggerFactory
from multithreading.threading import HttpClient

BASE_DIR = pathlib.Path(__file__).parent.resolve()

config_file = BASE_DIR / 'log.yaml'


def do_something():
    LoggerFactory(config_file=config_file)  # For do_something function, LoggerFactory is used
    arr = [1, 2, 3, 4]
    logging.info(f'Array elements: {arr}')
    count = 0
    try:
        while True:
            if count >= len(arr):
                break
            else:
                result = arr[count] / (count + 1)
                count += 1
                logging.info(
                    f"Array element: {arr[count]} and index: {count}. Result: {result}", )
    except IndexError:
        logging.exception(
            exc_info=False, msg=f"array length: {len(arr)} and index: {count}. Index {len(arr) - 1} < Index {count}. "
                                f"Index out of bound")
    except Exception as e:
        logging.exception(e.__str__())


def basic_logger_config(name):
    """
    Basic logger configuration
    """
    logging.basicConfig(
        format='%(asctime)s - [%(levelname)s] - [%(name)s] - [%(threadName)s] - %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
        stream=sys.stdout
    )
    return logging.getLogger(name)


class Test:
    logger = basic_logger_config(__name__)

    def __init__(self):
        self.client = HttpClient()
        self.logger.info('Initializing Test Class')
        logging.getLogger("chardet.charsetprober").disabled = True

    def print_something(self):
        self.logger.info(f'Printing something. From {self.__class__.__name__}')

    def call_http(self):
        self.logger.info(f'Calling http. From {self.__class__.__name__}')
        return self.client.get('https://jsonplaceholder.typicode.com/posts')


def io_calls(num_of_calls):
    logging.info('Starting IO calls')
    start = time.time()
    for i in range(num_of_calls):
        test = Test()
        result = test.call_http()
        logging.info(f'Result: {result.json()}')
    logging.info(f'elapsed time: {time.time() - start}')
    logging.info('Ending IO calls')


if __name__ == '__main__':
    # load_logging_config()
    do_something()
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(io_calls, range(2))
