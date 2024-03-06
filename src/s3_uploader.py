import boto3
import os
from tqdm import tqdm

class S3Uploader:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    def upload_files(self, file_paths, s3_folder=''):
        for file_path in file_paths:
            s3_key = os.path.join(s3_folder, os.path.basename(file_path))
            try:
                with tqdm(total=os.path.getsize(file_path), unit='B', unit_scale=True, desc=f"Uploading {file_path}") as pbar:
                    self.s3.upload_file(file_path, self.bucket_name, s3_key, Callback=pbar.update)
                return f"File uploaded successfully to S3 bucket: {self.bucket_name}/{s3_key}"
            except Exception as e:
                return f"Error uploading file {file_path} to S3: {e}"
