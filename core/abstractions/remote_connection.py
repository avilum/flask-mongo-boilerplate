from abc import abstractmethod, ABCMeta


class RemoteConnection(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def connect(self):
        raise NotImplementedError()

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError()
