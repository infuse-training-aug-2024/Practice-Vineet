import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
@app.route(route="email_validation", methods = ["GET"])

def email_validation(req: func.HttpRequest) -> func.HttpResponse:

    email = req.headers.get("email")

    if not email:

        response_body = {

            "status" : "Error",

            "message" : "Invalid request. Email is missing"

        }

        return func.HttpResponse(

            json.dumps(response_body),

            status_code= 400,

            mimetype = "application/json"

        )

   

    allowed_emails = ["vineet@gmail.com"]



    if email in allowed_emails:

        response_body = {

            "status": "success",

            "message": "Email authenticated"

        }

        return func.HttpResponse(

            json.dumps(response_body),

            status_code=200,

            mimetype = "application/json"

        )

    else:

        response_body = {

            "status": "failure",

            "message": "Email authentication failed"

        }

        return func.HttpResponse(

            json.dumps(response_body),

            status_code=403,

            mimetype = "application/json"

        )