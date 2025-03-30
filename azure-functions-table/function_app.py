import logging
import json
import os
from azure.data.tables import TableServiceClient, TableEntity
import azure.functions as func
 
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
 
# CRUD Functions
@app.route(route="table_operations", methods=["POST"])
def create_item(req: func.HttpRequest) -> func.HttpResponse:
    try:
        table_name = req.params.get("table_name")
        if not table_name:
            logging.error("table_name parameter is missing in the request.")
            return func.HttpResponse("Please provide the 'table_name' parameter in the query string.", status_code=400)
 
        data = req.get_json()
       
        table_service_client = TableServiceClient.from_connection_string(os.getenv("CONN_STR"))
        table_client = table_service_client.get_table_client(table_name)
       
        table_client.create_entity(entity=data)
       
        return func.HttpResponse(json.dumps({"status": "Entity created successfully"}), status_code=201)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
 
@app.route(route="table_operations", methods=["GET"])
def read_item(req: func.HttpRequest) -> func.HttpResponse:
    try:
        table_name = req.params.get("table_name")
        if not table_name:
            logging.error("table_name parameter is missing in the request.")
            return func.HttpResponse("Please provide the 'table_name' parameter in the query string.", status_code=400)
       
        partition_key = req.params.get('PartitionKey')
        row_key = req.params.get('RowKey')
 
        table_service_client = TableServiceClient.from_connection_string(os.getenv("CONN_STR"))
        table_client = table_service_client.get_table_client(table_name)
       
        entity = table_client.get_entity(partition_key, row_key)
       
        return func.HttpResponse(json.dumps(entity), status_code=200)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=404)
 
@app.route(route="table_operations", methods=["PUT"])
def update_item(req: func.HttpRequest) -> func.HttpResponse:
    try:
        table_name = req.params.get("table_name")
        if not table_name:
            logging.error("table_name parameter is missing in the request.")
            return func.HttpResponse("Please provide the 'table_name' parameter in the query string.", status_code=400)
       
        data = req.get_json()
        partition_key = data["PartitionKey"]
        row_key = data["RowKey"]
       
        table_service_client = TableServiceClient.from_connection_string(os.getenv("CONN_STR"))
        table_client = table_service_client.get_table_client(table_name)
       
        entity = table_client.get_entity(partition_key, row_key)
       
        for key, value in data.items():
            if key not in ["PartitionKey", "RowKey"]:
                entity[key] = value
       
        table_client.update_entity(entity)
       
        return func.HttpResponse(json.dumps({"status": "Entity updated successfully"}), status_code=200)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
 
@app.route(route="table_operations", methods=["DELETE"])
def delete_item(req: func.HttpRequest) -> func.HttpResponse:
    try:
        table_name = req.params.get("table_name")
        if not table_name:
            logging.error("table_name parameter is missing in the request.")
            return func.HttpResponse("Please provide the 'table_name' parameter in the query string.", status_code=400)
           
        partition_key = req.params.get('PartitionKey')
        row_key = req.params.get('RowKey')
 
        table_service_client = TableServiceClient.from_connection_string(os.getenv("CONN_STR"))
        table_client = table_service_client.get_table_client(table_name)
       
        table_client.delete_entity(partition_key, row_key)
       
        return func.HttpResponse(json.dumps({"status": "Entity deleted successfully"}), status_code=200)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
 
@app.route(route="table_operations", methods=["OPTIONS"])
def options(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(status_code=200)