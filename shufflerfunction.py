import azure.functions as func
import json
from collections import defaultdict

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        mapped_data = data.get("mapped_data", [])
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    # Group by word
    grouped_data = defaultdict(list)
    for item in mapped_data:
        grouped_data[item["key"]].append(item["value"])

    # Convert to dictionary
    grouped_data = dict(grouped_data)

    return func.HttpResponse(json.dumps(grouped_data), status_code=200, mimetype="application/json")
