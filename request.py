import requests

# Replace with your Azure Function URL
url = "https://saadapp.azurewebsites.net/api/http_trigger?code=vSRpJJuQHGwaVtDDREzZpXGFllFQEHoV-N8-71Mo7VeOAzFuCWBp7A%3D%3D"
payload = {
    "lower": 0,
    "upper": 3.14
}

# Send the POST request
response = requests.post(url, json=payload)

# Print the response
print(response.status_code)
print(response.json())
