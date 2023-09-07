import requests

# Define the API endpoint URL
url = "http://localhost:8000/chess/knight"

# Define the JSON payload
payload = {
    "Positions": {
        "Knight": "C3"
    }
}

# Send the POST request
response = requests.post(url, json=payload)

# Check the response
if response.status_code == 200:
    data = response.json()
    print("Valid Moves:", data["valid_moves"])
else:
    print("Error:", response.text)
