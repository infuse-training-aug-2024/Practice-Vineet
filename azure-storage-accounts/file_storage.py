from azure.storage.fileshare import ShareServiceClient
from dotenv import load_dotenv
import os
load_dotenv()
class FileShareManager:
    def __init__(self):
        conn_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.share_service_client = ShareServiceClient.from_connection_string(conn_string)
 
    def create_share(self, share_name):
        try:
            share_client = self.share_service_client.create_share(share_name)
            print(f"File Share '{share_name}' created.")
        except Exception as e:
            print(f"An error occurred while creating the file share: {e}")
        return share_client
 
    def upload_file(self, share_name, file_path, dest_file_name):
        try:
            share_client = self.share_service_client.get_share_client(share_name)
            dir_client = share_client.get_directory_client("")
            file_client = dir_client.get_file_client(dest_file_name)
           
            with open(file_path, "rb") as source_file:
                file_client.upload_file(source_file)
           
            print(f"File '{dest_file_name}' uploaded to share '{share_name}'.")
        except Exception as e:
            print(f"An error occurred while uploading the file: {e}")
 
    def download_file(self, share_name, dest_file_name, download_path):
        try:
            share_client = self.share_service_client.get_share_client(share_name)
            dir_client = share_client.get_directory_client("")
            file_client = dir_client.get_file_client(dest_file_name)
           
            with open(download_path, "wb") as download_file:
                download_stream = file_client.download_file()
                download_file.write(download_stream.readall())
           
            print(f"File '{dest_file_name}' downloaded to '{download_path}'.")
        except Exception as e:
            print(f"An error occurred while downloading the file: {e}")
 
    def list_files_in_share(self, share_name):
        try:
            share_client = self.share_service_client.get_share_client(share_name)
            dir_client = share_client.get_directory_client("")
            files = dir_client.list_directories_and_files()
 
            print(f"Files in share '{share_name}':")
            for file_item in files:
                print(f"- {file_item['name']}")
        except Exception as e:
            print(f"An error occurred while listing files: {e}")
 
 
 
file_share_manager = FileShareManager()
 
file_share_manager.create_share("myfileshare")
 
file_share_manager.upload_file("myfileshare", "local_file.txt", "uploaded_file.txt")
 
file_share_manager.download_file("myfileshare", "uploaded_file.txt", "downloaded_file.txt")
 
file_share_manager.list_files_in_share("myfileshare")