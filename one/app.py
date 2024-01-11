import requests
import os
import rarfile

def download_large_file(url, destination_path, chunk_size=8192):
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(destination_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                file.write(chunk)

def create_rar_files(input_file_path, output_directory, num_files, file_size):
    with rarfile.RarFile(input_file_path, 'r') as large_rar:
        for i in range(num_files):
            output_file_path = os.path.join(output_directory, f'output_file_{i + 1}.rar')
            with rarfile.RarFile(output_file_path, 'w') as output_rar:
                current_size = 0
                while current_size < file_size:
                    member = large_rar.namelist()[0]  # Assuming there is only one file in the large RAR
                    data = large_rar.read(member, size=file_size - current_size)
                    output_rar.writestr(member, data)
                    current_size += len(data)

if __name__ == "__main__":
    large_file_url = "https://drive.usercontent.google.com"
    large_file_destination = "./"
    output_directory = "./"
    num_files = 10
    file_size = 1 * 1024 * 1024 * 1024  # 1.5 GB in bytes

    # Download the large file
    download_large_file(large_file_url, large_file_destination)

    # Create 10 RAR files
    create_rar_files(large_file_destination, output_directory, num_files, file_size)
