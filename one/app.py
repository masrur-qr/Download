import os
from zipfile import ZipFile

def split_zip(input_file, output_directory, chunk_size):
    with ZipFile(input_file, 'r') as zip_archive:
        file_size = os.path.getsize(input_file)
        num_chunks = (file_size + chunk_size - 1) // chunk_size

        for i in range(num_chunks):
            start = i * chunk_size
            end = min((i + 1) * chunk_size, file_size)
            chunk_name = f"{os.path.splitext(os.path.basename(input_file))[0]}_chunk{i + 1}.zip"
            chunk_path = os.path.join(output_directory, chunk_name)

            with ZipFile(chunk_path, 'w') as chunk_zip:
                for file_info in zip_archive.infolist():
                    with zip_archive.open(file_info.filename) as file_in_zip:
                        chunk_zip.writestr(file_info, file_in_zip.read())

if __name__ == "__main__":
    input_file_path = "static/your_large_file.zip"  # Update with your actual file path
    output_directory = "static/chunks"
    chunk_size = 1024 * 1024 * 1024  # 1 GB in bytes

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    split_zip(input_file_path, output_directory, chunk_size)
