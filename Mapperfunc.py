import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Parse input data
    try:
        data = req.get_json()
        input_lines = data.get("lines", [])
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    # Perform mapping: Convert lines into <word, 1> pairs
    mapped_data = []
    for line in input_lines:
        words = line.split()
        for word in words:
            mapped_data.append({"key": word, "value": 1})

    return func.HttpResponse(json.dumps(mapped_data), status_code=200, mimetype="application/json")
