from abc import ABCMeta

from core.configurations.env import DEVELOP_MODE


class MongoDbConfiguration(object):
    __metaclass__ = ABCMeta

    DATABASE_NAME = ''
    HOST = None
    PORT = None
    USERNAME = None
    PASSWORD = None
    AUTH_DB = 'admin'
    COLLECTION = ''


# TODO: Configure
class ProductionDbConfiguration(MongoDbConfiguration):
    HOST = ''
    PORT = 27017
    USERNAME = ''
    PASSWORD = ''
    COLLECTION = ''


# TODO: Configure
class TestDbConfiguration(MongoDbConfiguration):
    HOST = ''
    PORT = 27017
    USERNAME = ''
    PASSWORD = ''
    COLLECTION = ''


DEFAULT_DB_CONFIGURATION = TestDbConfiguration if DEVELOP_MODE else ProductionDbConfiguration
