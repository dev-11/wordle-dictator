import config
import repositories.environment_repository as er
import repositories.s3_repository as s3r

from .storage_service import StorageService
from .secret_manager_service import SecretManagerService
from .wordle_dictator_service import WordleDictatorService


class ServiceFactory:
    def __init__(self):
        """Service to create every service."""
        repo = s3r.S3Repository(config.data_bucket)
        env_repo = er.EnvironmentRepository()

        self._storage_service = StorageService(repo)
        self._secret_manager = SecretManagerService(env_repo)

    def create_wordle_dictator_service(self):
        return WordleDictatorService()
