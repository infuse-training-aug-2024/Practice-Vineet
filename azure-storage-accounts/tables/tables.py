from azure.data.tables import TableServiceClient, TableClient
from azure.core.credentials import AzureNamedKeyCredential
import datetime
from dotenv import load_dotenv
import os

class AzureTableOperations:
    def __init__(self, connection_string):
        """Initialize Azure Table Storage client"""
        self.connection_string = connection_string
        self.table_service = TableServiceClient.from_connection_string(connection_string)
        
    def create_table(self, table_name):
        """Create a new table if it doesn't exist"""
        try:
            table_client = self.table_service.create_table(table_name)
            print(f"Table '{table_name}' created successfully")
            return table_client
        except Exception as e:
            print(f"Error creating table: {e}")
            return None

    def insert_entity(self, table_name, entity):
        """Create a new entity in the table"""
        try:
            table_client = self.table_service.get_table_client(table_name)
            table_client.create_entity(entity=entity)
            print(f"Entity inserted successfully")
        except Exception as e:
            print(f"Error inserting entity: {e}")

    def get_entity(self, table_name, partition_key, row_key):
        """Read an entity from the table"""
        try:
            table_client = self.table_service.get_table_client(table_name)
            entity = table_client.get_entity(partition_key=partition_key, row_key=row_key)
            return entity
        except Exception as e:
            print(f"Error retrieving entity: {e}")
            return None

    def update_entity(self, table_name, entity):
        """Update an existing entity in the table"""
        try:
            table_client = self.table_service.get_table_client(table_name)
            table_client.update_entity(mode='merge', entity=entity)
            print(f"Entity updated successfully")
        except Exception as e:
            print(f"Error updating entity: {e}")

    def delete_entity(self, table_name, partition_key, row_key):
        """Delete an entity from the table"""
        try:
            table_client = self.table_service.get_table_client(table_name)
            table_client.delete_entity(partition_key=partition_key, row_key=row_key)
            print(f"Entity deleted successfully")
        except Exception as e:
            print(f"Error deleting entity: {e}")

    def query_entities(self, table_name, filter_query=None):
        """Query entities from the table with optional filter"""
        try:
            table_client = self.table_service.get_table_client(table_name)
            entities = table_client.query_entities(filter_query)
            return list(entities)
        except Exception as e:
            print(f"Error querying entities: {e}")
            return []

def main():

    load_dotenv()
    # Replace with your Azure Storage Account connection string
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING_TABLES")
    
    # Initialize the table operations class
    table_ops = AzureTableOperations(connection_string)
    
    # Create a new table
    table_name = "vineettable"
    table_ops.create_table(table_name)
    
    # Create a new employee entity
    new_employee = {
        'PartitionKey': 'IT',
        'RowKey': 'emp001',
        'Name': 'Vineet Sawant',
        'Email': 'Vineet.Sawant@example.com',
        'HireDate': datetime.datetime.now().isoformat()
    }
    
    # Insert the entity
    table_ops.insert_entity(table_name, new_employee)
    
    # Read the entity
    employee = table_ops.get_entity(table_name, 'IT', 'emp001')
    if employee:
        print("Retrieved employee:", dict(employee))
    
    # Update the entity
    employee['Email'] = 'Vineet.Sawant.updated@example.com'
    table_ops.update_entity(table_name, employee)
    
    # Query entities
    query = "PartitionKey eq 'IT'"
    results = table_ops.query_entities(table_name, query)
    print("Query results:", results)
    
    # Delete the entity
    table_ops.delete_entity(table_name, 'IT', 'emp001')

if __name__ == "__main__":
    main()