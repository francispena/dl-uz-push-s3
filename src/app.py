import os
from file_downloader import FileDownloader
from file_unzipper import FileUnzipper
from s3_uploader import S3Uploader
from datetime import datetime
import argparse

def download_file(url, download_dir, download_file):
    fileDownloader = FileDownloader(url)
    ret_val = fileDownloader.download_file(download_dir, download_file)
    return ret_val

def unzip_file(gz_file_path, unzipped_file_dir, unzipped_file):
    unzipper = FileUnzipper(gz_file_path, unzipped_file_dir, unzipped_file)
    ret_val = unzipper.unzip()
    return ret_val

def upload_file_to_s3(bucket_name, file_paths):
    uploader = S3Uploader(bucket_name)
    retval = uploader.upload_files(file_paths)
    return retval

def delete_files(file_paths):
    for file_path in file_paths:
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully")
        except OSError as e:
            print(f"Error deleting file '{file_path}': {e}")

# Initialize Argument Parser
parser = argparse.ArgumentParser(description="Download URL")
# Add URL Argument
parser.add_argument("url", type=str, help="URL to be processed")
# Parse Arguments
args = parser.parse_args()
# Access URL Argument Value
url = args.url
print("URL:", url)

current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# URL and file paths
#url = 'https://getsamplefiles.com/download/gzip/sample-1.gz'
download_dir = "./downloaded_files"
download_filename = "downloaded_file.gz"
unzipped_file_dir = "./unzipped_files"
unzipped_filename = f'output_{current_datetime}.json'
bucket_name = 'unzippedjsonfiles'

# Download the file
ret_val = download_file(url, download_dir, download_filename)
print(ret_val)
if ret_val != "File downloaded successfully.":
    exit()

# Unzip the file
gz_file_path = os.path.join(download_dir, download_filename)
ret_val = unzip_file(gz_file_path, unzipped_file_dir, unzipped_filename)
print(ret_val)
if ret_val != "File successfully unzipped.":
    exit()

# Upload the file to S3
file_paths = [os.path.join(unzipped_file_dir, unzipped_filename)] #store in array just in case we need in future
retval = upload_file_to_s3(bucket_name, file_paths)
print(retval)
if "successfully" in retval:
    print("Process was successful")
    # Delete files
    delete_files(file_paths + [gz_file_path])
