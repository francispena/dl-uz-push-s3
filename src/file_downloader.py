import os
import requests
from tqdm import tqdm

class FileDownloader:
    def __init__(self, url: str):
        self.url = url

    def download_file(self, output_dir: str, output_file: str) -> str:
        try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
        
            file_size = 0
            output_path = os.path.join(output_dir, output_file)
            # Check if the file exists
            if not os.path.exists(output_path):
                headers = {"Range": "bytes=0-"}  # Download the entire file from the beginning
            else:
                # If the file exists, get its size
                file_size = os.path.getsize(output_path)
                headers = {"Range": f"bytes={file_size}-"}  # Resume download from the end of the existing file

            response = requests.get(self.url, headers=headers, stream=True)

            if response.status_code == 206:  # Partial Content response
                mode = 'ab'  # Append mode to resume writing at the end of the existing file
            elif response.status_code == 200:  # Full Content response
                mode = 'wb'
            else:
                return "Failed to download file."

            total_size = int(response.headers.get('content-length', 0))
            if file_size > 0 and total_size == file_size:
                return "File downloaded successfully." 
            with open(output_path, mode) as f:
                with tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading", initial=file_size, ascii=True) as pbar:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))

            ret_val = "File downloaded successfully."
        except Exception as e:
            ret_val = f"Error: Failed to unzip file - {e}"
        
        return ret_val