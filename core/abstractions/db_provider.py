from abc import abstractmethod

from core.abstractions.remote_connection import RemoteConnection


class DbProvider(RemoteConnection):

    @abstractmethod
    def get_obj(self, object_id):
        raise NotImplementedError()

    @abstractmethod
    def insert_obj(self, object_id):
        raise NotImplementedError()

    @abstractmethod
    def connect(self):
        raise NotImplementedError()

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError()
