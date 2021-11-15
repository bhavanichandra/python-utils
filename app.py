import logging
from logger.logger import log
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.resolve()

config_file = BASE_DIR / 'log.yaml'


@log(config_file=config_file.__str__())
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


@log(config_file=config_file.__str__())
class Test:
    def __init__(self):
        logging.info('Initializing Test Class')

    def print_something(self):
        logging.info(f'Printing something. From {self.__class__.__name__}')


if __name__ == '__main__':
    # load_logging_config()
    # do_something()
    test = Test()
    test.print_something()
