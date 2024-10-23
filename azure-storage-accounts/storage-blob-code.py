# from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
# import os
# from datetime import datetime
# from dotenv import load_dotenv

# def azure_blob_operations(connection_string, container_name, local_file_path, blob_name):
#     try:
#         blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
#         print("\n1. Creating container...")
#         container_client = blob_service_client.create_container(container_name)
#         print(f"Container '{container_name}' created successfully")
        
#         print("\n2. Uploading blob...")
#         with open(local_file_path, "rb") as data:
#             blob_client = blob_service_client.get_blob_client(
#                 container=container_name,
#                 blob=blob_name
#             )
#             blob_client.upload_blob(data)
#         print(f"Blob '{blob_name}' uploaded successfully")
    

#         print("\n3. Listing blobs in container...")
#         container_client = blob_service_client.get_container_client(container_name)
#         blob_list = container_client.list_blobs()
#         for blob in blob_list:
#             print(f"\tBlob name: {blob.name}")
        

#         print("\n4. Downloading blob...")
#         download_file_path = f"downloaded_{blob_name}"
#         blob_client = blob_service_client.get_blob_client(
#             container=container_name,
#             blob=blob_name
#         )
        
#         with open(download_file_path, "wb") as download_file:
#             download_file.write(blob_client.download_blob().readall())
#         print(f"Blob downloaded to: {download_file_path}")
        
#         print("\n5. Adding metadata to blob...")
#         metadata = {
#             'created': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
#             'category': 'test',
#             'owner': 'vineet'
#         }
#         blob_client.set_blob_metadata(metadata=metadata)
#         print("Metadata added successfully")
        
#         properties = blob_client.get_blob_properties()
#         print("\nBlob metadata:")
#         for key, value in properties.metadata.items():
#             print(f"\t{key}: {value}")
            
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# def main():
#     load_dotenv()

#     AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
#     connection_string = AZURE_STORAGE_CONNECTION_STRING
#     container_name = "mycontainer"
#     local_file_path = "C:/Users/vineet.sawant/Desktop/Practice-Vineet/azure-storage-accounts/sample_blob.txt"
#     blob_name = "sample_blob.txt"
    
#     if not os.path.exists(local_file_path):
#         with open(local_file_path, "w") as f:
#             f.write("This is a sample file for Azure Blob Storage testing.")
    
#     azure_blob_operations(
#         connection_string=connection_string,
#         container_name=container_name,
#         local_file_path=local_file_path,
#         blob_name=blob_name
#     )

# if __name__ == "__main__":
#     main()

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
from datetime import datetime
from dotenv import load_dotenv

class AzureBlobManager:
    """
    A class to manage Azure Blob Storage operations including container creation,
    blob upload/download, listing blobs, and metadata management.
    """
    
    def __init__(self, connection_string):
        """
        Initialize the AzureBlobManager with a connection string.
        
        Args:
            connection_string (str): Azure Storage account connection string
        """
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    def create_container(self, container_name):
        """
        Create a new container in the storage account.
        
        Args:
            container_name (str): Name of the container to create
            
        Returns:
            ContainerClient: The created container client
        """
        try:
            print(f"\nCreating container '{container_name}'...")
            container_client = self.blob_service_client.create_container(container_name)
            print(f"Container '{container_name}' created successfully")
            return container_client
        except Exception as e:
            print(f"Error creating container: {str(e)}")
            raise
    
    def upload_blob(self, container_name, local_file_path, blob_name):
        """
        Upload a file to the specified container as a blob.
        
        Args:
            container_name (str): Name of the container
            local_file_path (str): Path to the local file
            blob_name (str): Name to give the blob
        """
        try:
            print(f"\nUploading blob '{blob_name}'...")
            with open(local_file_path, "rb") as data:
                blob_client = self.blob_service_client.get_blob_client(
                    container=container_name,
                    blob=blob_name
                )
                blob_client.upload_blob(data)
            print(f"Blob '{blob_name}' uploaded successfully")
            return blob_client
        except Exception as e:
            print(f"Error uploading blob: {str(e)}")
            raise
    
    def list_blobs(self, container_name):
        """
        List all blobs in the specified container.
        
        Args:
            container_name (str): Name of the container
        """
        try:
            print(f"\nListing blobs in container '{container_name}'...")
            container_client = self.blob_service_client.get_container_client(container_name)
            blob_list = container_client.list_blobs()
            for blob in blob_list:
                print(f"\tBlob name: {blob.name}")
            return blob_list
        except Exception as e:
            print(f"Error listing blobs: {str(e)}")
            raise
    
    def download_blob(self, container_name, blob_name, download_file_path=None):
        """
        Download a blob from the specified container.
        
        Args:
            container_name (str): Name of the container
            blob_name (str): Name of the blob to download
            download_file_path (str, optional): Path where to save the downloaded file
        """
        try:
            if download_file_path is None:
                download_file_path = f"downloaded_{blob_name}"
            
            print(f"\nDownloading blob '{blob_name}'...")
            blob_client = self.blob_service_client.get_blob_client(
                container=container_name,
                blob=blob_name
            )
            
            with open(download_file_path, "wb") as download_file:
                download_file.write(blob_client.download_blob().readall())
            print(f"Blob downloaded to: {download_file_path}")
        except Exception as e:
            print(f"Error downloading blob: {str(e)}")
            raise
    
    def set_blob_metadata(self, container_name, blob_name, metadata=None):
        """
        Set metadata for a specific blob.
        
        Args:
            container_name (str): Name of the container
            blob_name (str): Name of the blob
            metadata (dict, optional): Dictionary of metadata to set
        """
        try:
            if metadata is None:
                metadata = {
                    'created': datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),
                    'category': 'test',
                    'owner': 'vineet'
                }
            
            print(f"\nAdding metadata to blob '{blob_name}'...")
            blob_client = self.blob_service_client.get_blob_client(
                container=container_name,
                blob=blob_name
            )
            blob_client.set_blob_metadata(metadata=metadata)
            print("Metadata added successfully")
            
            # Get and display the metadata
            properties = blob_client.get_blob_properties()
            print("\nBlob metadata:")
            for key, value in properties.metadata.items():
                print(f"\t{key}: {value}")
        except Exception as e:
            print(f"Error setting blob metadata: {str(e)}")
            raise

def main():
    # Load environment variables
    load_dotenv()
    
    # Get connection string from environment variables
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    if not connection_string:
        raise ValueError("Azure Storage connection string not found in environment variables")
    
    # Initialize parameters
    container_name = "mycontainer"
    local_file_path = "sample_blob.txt"
    blob_name = "sample_blob.txt"
    
    # Create sample file if it doesn't exist
    if not os.path.exists(local_file_path):
        with open(local_file_path, "w") as f:
            f.write("This is a sample file for Azure Blob Storage testing.")
    
    try:
        # Initialize the blob manager
        blob_manager = AzureBlobManager(connection_string)
        
        # Perform operations
        blob_manager.create_container(container_name)
        blob_manager.upload_blob(container_name, local_file_path, blob_name)
        blob_manager.list_blobs(container_name)
        blob_manager.download_blob(container_name, blob_name)
        blob_manager.set_blob_metadata(container_name, blob_name)
        
    except Exception as e:
        print(f"An error occurred in main: {str(e)}")

if __name__ == "__main__":
    main()


