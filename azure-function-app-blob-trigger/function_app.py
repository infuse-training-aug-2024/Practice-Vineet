import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="blobtriggervineet",
                               connection="storagevineet_STORAGE") 
def blob_trigger_vineet(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
