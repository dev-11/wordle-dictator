import config
import repositories.s3_repository as s3r

from .storage_service import StorageService
from .wordle_dictator_service import WordleDictatorService
from .random_service import RandomService


class ServiceFactory:
    @staticmethod
    def create_storage_service():
        repo = s3r.S3Repository(config.data_bucket)
        return StorageService(repo)

    @staticmethod
    def create_random_service():
        return RandomService()

    def create_wordle_dictator_service(self):
        return WordleDictatorService(self.create_storage_service(), self.create_random_service())
