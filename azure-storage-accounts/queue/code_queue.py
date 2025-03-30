from azure.storage.queue import QueueServiceClient
from azure.core.exceptions import ResourceExistsError
from dotenv import load_dotenv
import os
import json
 
load_dotenv()
 
class AzureQueueClient:
    def __init__(self, queue_name):
        self.conn_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.queue_name = queue_name
        self.queue_client = self._create_or_get_queue()
 
    def _create_or_get_queue(self):
        queue_service_client = QueueServiceClient.from_connection_string(self.conn_string)
        try:
            queue_client = queue_service_client.create_queue(self.queue_name)
            print(f"Queue '{self.queue_name}' created successfully.")
        except ResourceExistsError:
            queue_client = queue_service_client.get_queue_client(self.queue_name)
            print(f"Queue '{self.queue_name}' already exists.")
        return queue_client
 
    def send_message(self, message_content):
        self.queue_client.send_message(message_content)
        print(f"Sent message: {message_content}")
 
    def send_object(self, obj):
        message_content = json.dumps(obj)
        self.queue_client.send_message(message_content)
        print(f"Sent object: {obj}")
 
    def peek_message(self):
        peeked_messages = self.queue_client.peek_messages()
        for message in peeked_messages:
            print(f"Peeked message: {message.content}")
            return message.content
 
    def receive_and_delete_message(self):
        messages = self.queue_client.receive_messages()
        for message in messages:
            print(f"Received message: {message.content}")
            self.queue_client.delete_message(message)
            print("Message deleted.")
            return message.content
 
    def receive_and_delete_object(self):
        messages = self.queue_client.receive_messages()
        for message in messages:
            obj = json.loads(message.content)
            print(f"Received object: {obj}")
            self.queue_client.delete_message(message)
            print("Message deleted.")
            return obj
# Usage
if __name__ == "__main__":
 
    queue_name = "sample-queue"
 
    azure_queue_client = AzureQueueClient(queue_name)
    azure_queue_client.send_message("Hello, !")
    azure_queue_client.peek_message()
    azure_queue_client.receive_and_delete_message()
 
    sample_object = {
    "name": "John Wick",
    "age": 60,
    "email": "johnwick@example.com"
    }
    azure_queue_client.send_object(sample_object)
    received_obj = azure_queue_client.receive_and_delete_object()
    print(f"Received object: {received_obj}")