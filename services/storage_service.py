from datetime import datetime as dt

from repositories import S3Repository


class StorageService:
    def __init__(self, repo: S3Repository):
        """Service to store/read data."""
        self._repo = repo

    def has_key(self, key):
        return self._repo.has_key(key)

    def get_lines(self, key):
        data = self._repo.get_body(key).splitlines()
        return data

    def save_or_update(self, key, data):
        return self._repo.save_or_update_file(key, data)
