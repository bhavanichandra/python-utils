This repo contains various utility and example packages

- Logger
- Database
- Multithreading

## Logger

- This python module have a [logger.py](logger/logger.py) file and a config folder
- The [logger.py](logger/logger.py) file contains log and log_v1 decorators
- The config folder contains a various examples of logging configurations in yaml file
- For the usage of the decorator, please check [app.py](app.py). The `@log` decorator is used on both
  the `do_something()` function and `Test` Class
- New addition to [logger.py](logger/logger.py) is the LoggerFactory class, which initialize the logger with the
  configuration file and name of the logger.

## Multithreading

- This package contains a [threading.py](threading/threading.py) file.
- The [threading.py](threading/threading.py) file contains a HttpClient build using requests library and used Threading
  library to make the requests concurrent.
- Please check the [app.py](app.py) file on how to use the HttpClient.

## Database

- This package contains a [database.py](database/database.py) file.
- The [database.py](database/database.py) file contains a Database class which is used to connect to the Mongo DB
  database and execute the dependent queries with transactions enabled
- Please check [app.py](app.py) file on how to use the Database class.


