import logging
import os
import pathlib
import sys
import time

from pymongo.client_session import ClientSession
from pymongo.collection import Collection

# from concurrent.futures import ThreadPoolExecutor
from bson.json_util import dumps
import json
from database.db import Database, Employee
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


connection_str = str(os.getenv('MONGO_DB_URL'))
database = Database(connection_str=connection_str, db_name='employee_directory')


def execute_db_statements(session: ClientSession, collection: Collection):
    emp = Employee(name='Bhavani Chandra', email='bhavanichandra9@gmail.com', mobile='9989789012')
    inserted_id = collection.insert_one(emp.to_mongo(), session=session)
    logging.info(f"Employee data: {emp.__str__()} is inserted: {inserted_id.inserted_id}")
    fetch_emp = collection.find({'_d': inserted_id.inserted_id}, session=session)
    return json.loads(dumps(fetch_emp)), inserted_id.inserted_id


if __name__ == '__main__':
    result = database.execute_db_operations(execute_db_statements, Employee.collection())
    print(result)
# load_logging_config()
# do_something()
# with ThreadPoolExecutor(max_workers=3) as executor:
#     executor.map(io_calls, range(2))
