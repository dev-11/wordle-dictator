import boto3
from botocore.errorfactory import ClientError


class S3Repository:
    def __init__(self, bucket):
        """S3 repo, needs a bucket to operate on."""
        self._bucket = bucket
        self._s3 = boto3.resource("s3")

    def get_body(self, key):
        obj = self._s3.Object(self._bucket, key)
        body = obj.get()["Body"].read()
        return body

    def has(self, key):
        try:
            self._s3.Bucket(self._bucket).Object(key).last_modified
        except ClientError:
            return False
        return True

    def save_or_update_file(self, key, body):
        try:
            obj = self._s3.Object(self._bucket, key)
            obj.put(Body=body)

        except ClientError:
            return False
        return True
