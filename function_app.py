import azure.functions as func
import math
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger", methods=["POST"])
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Parse JSON input
        req_body = req.get_json()
        lower = float(req_body.get("lower", 0))
        upper = float(req_body.get("upper", 1))

        # Perform numerical integration
        result = numerical_integration(lower, upper)

        # Return the result as JSON
        return func.HttpResponse(
            json.dumps({"result": result}),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code=400
        )

# Numerical Integration Function
def numerical_integration(lower, upper):
    results = []  # Store results for different N
    N = 1
    while len(results) < 6:
        N *= 10  # Increase the number of intervals
        width = (upper - lower) / N
        total_area = 0.0
        for i in range(N):
            x = lower + i * width
            height = abs(math.sin(x))
            total_area += height * width
        results.append(total_area)
    return results
