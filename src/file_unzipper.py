import gzip
import os
from tqdm import tqdm

class FileUnzipper:
    def __init__(self, input_file: str, output_dir: str, output_file: str):
        self.input_file = input_file
        self.output_dir = output_dir
        self.output_file = output_file

    def unzip(self) -> str:
        try:
            # Check if the zip file exists
            if not os.path.exists(self.input_file):
                return f"Error: Zip file '{self.input_file}' does not exist."
            
            # Create the extraction directory if it doesn't exist
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
            
            output_path = os.path.join(self.output_dir, self.output_file)

            # Unzip the file
            with gzip.open(self.input_file, 'rb') as f_in:
                with open(output_path, 'wb') as f_out:
                    with tqdm(desc="Extracting", unit="B", unit_scale=True) as pbar:
                        while True:
                            chunk = f_in.read(1024)  # Read a chunk of data
                            if not chunk:  # End of file
                                break
                            f_out.write(chunk)  # Write the chunk to the output file
                            pbar.update(len(chunk))  # Update the progress bar with the size of the chunk

            return "File successfully unzipped."
            
        except Exception as e:
            return f"Error: Failed to unzip file - {e}"
            


