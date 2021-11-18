import logging

import mongoengine
from dotenv import load_dotenv
from mongoengine import Document, connect
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

load_dotenv()


# Models
class Employee(Document):
    name = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True)
    mobile = mongoengine.StringField()
    meta = {'collection': 'employee'}

    def __str__(self):
        return f'name: {self.name} | email: {self.email} | mobile: {self.mobile} '

    @staticmethod
    def collection():
        return 'employee'


# Database Transaction Class
class Database:
    def __init__(self, connection_str: str, db_name: str):
        """
        Initialize the database connection with mongo engine
        """
        self.client: MongoClient = connect(db=db_name, host=connection_str)
        self.database = self.client.get_database(name=db_name)
        self.session = self.client.start_session()

    def _commit_transaction(self):
        """
        Commit the transaction
        """
        try:
            self.session.commit_transaction()
        except (ConnectionFailure, OperationFailure) as ex:
            if ex.has_error_label("TransientTransactionError"):
                logging.info("TransientTransactionError")
                self._commit_transaction()
            else:
                raise

    def execute_db_operations(self, func: callable, collection_name: str):
        try:
            with self.session.start_transaction():
                collection = self.database.get_collection(collection_name)
                result = func(session=self.session, collection=collection)
                self._commit_transaction()
                return result
        except (ConnectionFailure, OperationFailure) as ex:
            if ex.has_error_label("TransientTransactionError"):
                logging.info("TransientTransactionError")
                self.execute_db_operations(func, collection)
            else:
                raise
