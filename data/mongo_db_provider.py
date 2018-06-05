from pymongo import MongoClient, DESCENDING
from core.abstractions.db_provider import DbProvider
from core.configurations.db import DEFAULT_DB_CONFIGURATION, MongoDbConfiguration
from core.logging.LoggerProvider import LoggerProvider


class MongoDbProvider(DbProvider):
    """
    Provides mongo db storing and reading methods.
    """

    def __init__(self, connection_configuration=None):
        """
        Initializes a new MongoDbProvider instance
        :param connection_configuration: The connection configuration
        :type connection_configuration: MongoDbConfiguration
        """
        self._logger = LoggerProvider.get_logger(self.__class__.__name__)
        if not connection_configuration:
            connection_configuration = DEFAULT_DB_CONFIGURATION
        if not issubclass(connection_configuration, MongoDbConfiguration):
            raise TypeError('The connection configuration must be of type MongoDbConfiguration.')
        self._connection_configuration = connection_configuration
        self.collection = None

    def connect(self):
        self._logger.debug('Connecting to the db.')
        self._client = MongoClient(self._connection_configuration.HOST, self._connection_configuration.PORT)
        self._db = self._client[self._connection_configuration.DATABASE_NAME]
        self._auth_db = self._client[self._connection_configuration.AUTH_DB]

        if self._connection_configuration.USERNAME and self._connection_configuration.PASSWORD:
            self._logger.info('Authenticating the db connection')
            self._auth_db.authenticate(self._connection_configuration.USERNAME, self._connection_configuration.PASSWORD)
            self._logger.info('Authenticated successfully.')

        self.collection = self._db[self._connection_configuration.COLLECTION]

    def close(self):
        self._client.close()

    def get_obj(self, object_id):
        # TODO: Implement
        raise NotImplementedError()

    def insert_obj(self, object_id):
        # TODO: Implement
        raise NotImplementedError()
