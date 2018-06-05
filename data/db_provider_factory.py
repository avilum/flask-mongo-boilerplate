from core.abstractions.db_provider import DbProvider
from core.configurations.db_provider import DEFAULT_DB_PROVIDER_CLASS, DEFAULT_DB_CONFIGURATION_CLASS


class DbProviderFactory(object):
    _DB_PROVIDER = None

    @classmethod
    def get_instance(self, db_provider_class=DEFAULT_DB_PROVIDER_CLASS, db_configuration=DEFAULT_DB_CONFIGURATION_CLASS):
        """
        Gets a default db provider instance.
        Creates one if it hasn't been created yet.
        :returns: DbProvider
        """
        if not db_provider_class or not issubclass(db_provider_class, DbProvider):
            raise TypeError('The db provider class must be of a subclass of {0}'.format(DbProvider.__name__))
        if not DbProviderFactory._DB_PROVIDER:
            DbProviderFactory._DB_PROVIDER = db_provider_class(db_configuration)
            DbProviderFactory._DB_PROVIDER.connect()
        return DbProviderFactory._DB_PROVIDER
