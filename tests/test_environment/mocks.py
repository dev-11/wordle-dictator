from unittest.mock import Mock

from repositories import S3Repository


def get_mocked_s3repo_returns_empty_body():
    s3r = S3Repository("test- bucket")
    s3r.get_body = Mock(name="get_body")
    s3r.get_body.return_value = b''  # in real life it's a byte string too
    s3r.get_metadata = Mock(name="get_metadata")
    s3r.get_metadata.return_value = ""
    s3r.has_key = Mock(name="has_key")
    s3r.has_key.return_value = False
    s3r.save_or_update_file = Mock(name="save_or_update_file")
    s3r.save_or_update_file.return_value = False
    return s3r


def get_mocked_s3repo_has_key_but_no_metadata():
    s3r = S3Repository("test-bucket")
    s3r.get_body = Mock(name="get_body")
    s3r.get_body.return_value = b''  # in real life it's a byte string too
    s3r.has_key = Mock(name="has_key")
    s3r.has_key.return_value = True
    s3r.save_or_update_file = Mock(name="save_or_update_file")
    s3r.save_or_update_file.return_value = False
    return s3r
