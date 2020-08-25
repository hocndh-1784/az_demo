from storages.backends.azure_storage import AzureStorage
from .settings import storage_account_name, storage_account_key


class AzureMediaStorage(AzureStorage):
    account_name = storage_account_name
    account_key = storage_account_key
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = storage_account_name
    account_key = storage_account_key
    azure_container = 'static'
    expiration_secs = None
