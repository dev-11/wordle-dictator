import unittest
from datetime import datetime as dt

from services import StorageService
from tests.test_environment import mocks


class StorageServiceTests(unittest.TestCase):
    def test_get_lines_returns_empty_array_when_repo_returns_empty_data(self):
        ss = StorageService(mocks.get_mocked_s3repo_returns_empty_body())
        result = ss.get_lines("test-key")
        self.assertEqual([], result)

    def test_save_or_update_returns_False_if_repo_cant_save_data(self):
        ss = StorageService(mocks.get_mocked_s3repo_returns_empty_body())
        result = ss.save_or_update("", "")
        self.assertFalse(result)
