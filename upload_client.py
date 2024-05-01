import boto3
import math

from config import Config
from models import StartUploadResponse


class UploadClient:

    s3 = None

    def __init__(self):

        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
            region_name=Config.AWS_DEFAULT_REGION,
        )

    def get_presigned_multipart(
        self,
        key: str,
        content_type: str,
        file_size: int,
        expires=3600,
        chunk_size=50 * 1024**2,
    ) -> StartUploadResponse:
        total_chunks = math.ceil(file_size / chunk_size)

        payload = {
            "ACL": "public-read",
            "Bucket": Config.AWS_STORAGE_BUCKET_NAME,
            "Key": key,
            "ContentType": content_type,
        }

        data = self.s3.create_multipart_upload(**payload)

        upload_id = data["UploadId"]

        urls = []

        for i in range(1, total_chunks + 1):
            signed_url = self.s3.generate_presigned_url(
                ClientMethod="upload_part",
                Params={
                    "Bucket": Config.AWS_STORAGE_BUCKET_NAME,
                    "Key": key,
                    "PartNumber": i,
                    "UploadId": upload_id,
                },
                ExpiresIn=expires,
            )
            urls.append(signed_url)

        return StartUploadResponse(
            urls=urls,
            chunk_size=chunk_size,
            key=key,
            upload_id=upload_id,
            fields={
                "Content-Type": content_type,
                "Key": key,
            },
        )

    def complete_multipart_upload(self, key: str, upload_id: str, etags_string: str):
        etags = etags_string.split(",")

        parts = [{"ETag": etags[i], "PartNumber": i + 1} for i in range(len(etags))]

        response = self.s3.complete_multipart_upload(
            Bucket=Config.AWS_STORAGE_BUCKET_NAME,
            Key=key,
            UploadId=upload_id,
            MultipartUpload={"Parts": parts},
        )

        return response
