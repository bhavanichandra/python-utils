
import functools
from mongoengine import connect
from pymongo import MongoClient


def singleton(cls):
    @functools.wraps(cls)
    def singleton_wrapper(*args, **kwargs):
        if singleton_wrapper.instance is None:
            singleton_wrapper.instance = cls(*args, **kwargs)
        return singleton_wrapper.instance
    singleton_wrapper.instance = None
    return singleton_wrapper


def mongo_connect(cls):
    def wrapper(*args, **kwargs):
        value: MongoClient = connect(db='employee_directory',
                                     host='mongodb+srv://api_user:QrOFOSkGENa1h51t@cluster0.yerkz.mongodb.net/')
        cls.mongo_client = value
        return cls(*args, **kwargs)
    return wrapper


@singleton
@mongo_connect
class Test:
    mongo_client: MongoClient

    def __init__(self):
        print('Initialized')

    def get_collection(self):
        print(self.mongo_client)


test = Test()
test2 = Test()

client = test.mongo_client
db = client.get_database('employee_directory')
employee_collection = db.get_collection('employee')
print(list(employee_collection.find({})))
