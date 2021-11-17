import logging
import pathlib
import time
from concurrent.futures import ThreadPoolExecutor

from logger.logger import LoggerFactory
from multithreading.threading import HttpClient

BASE_DIR = pathlib.Path(__file__).parent.resolve()

config_file = BASE_DIR / 'log.yaml'

LoggerFactory(config_file=config_file)


def do_something():
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


class Test:
    def __init__(self):
        self.client = HttpClient()
        logging.info('Initializing Test Class')

    def print_something(self):
        logging.info(f'Printing something. From {self.__class__.__name__}')

    def call_http(self):
        logging.info(f'Calling http. From {self.__class__.__name__}')
        return self.client.get('https://jsonplaceholder.typicode.com/posts')


def io_calls(num_of_calls):
    logging.info('Starting IO calls')
    start = time.time()
    for i in range(num_of_calls):
        test = Test()
        test.print_something()
        result = test.call_http()
        logging.info(f'Result: {result.json()}')
    logging.info(f'elapsed time: {time.time() - start}')
    logging.info('Ending IO calls')


if __name__ == '__main__':
    # load_logging_config()
    # do_something()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(io_calls, range(3))
