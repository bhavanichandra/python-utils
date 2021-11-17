import functools
import logging
import threading

import requests


def error_wrapper(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        try:
            return cls(*args, **kwargs)
        except Exception as e:
            logging.error(f'error: {e}')
            raise e

    return wrapper


@error_wrapper
class HttpClient:
    threading_local = threading.local()

    def __init__(self):
        if not hasattr(self.threading_local, 'http_session'):
            self.threading_local.http_session = requests.Session()


    def get(self, url: str, headers: dict = None) -> requests.Response:
        logging.info(f'HTTP GET: {url}')
        return self.threading_local.http_session.get(url, headers=headers)

    def post(self, url: str, data: dict, headers=None) -> requests.Response:
        if headers is None:
            headers = {'Content-Type': 'application/json'}
        return self.threading_local.http_session.post(url, data=data, headers=headers)

    def put(self, url: str, data: dict, headers=None) -> requests.Response:
        if headers is None:
            headers = {'Content-Type': 'application/json'}
        return self.threading_local.http_session.put(url, data=data, headers=headers)

    def delete(self, url: str, headers: dict = None) -> requests.Response:
        return self.threading_local.http_session.delete(url, headers=headers)

    def patch(self, url: str, data: dict, headers=None) -> requests.Response:
        if headers is None:
            headers = {'Content-Type': 'application/json'}
        return self.threading_local.http_session.patch(url, data=data, headers=headers)
