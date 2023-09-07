import requests
import json

# Define the data you want to send in the request
data = {
    "Positions":
     {
      "Queen":"H1",
      "Bishop":"B7",
      "Rook":"H8",
      "Knight":"F2"
     }
}

# Convert the data to JSON format
json_data = json.dumps(data)

# Define the URL for your Flask endpoint
url = 'http://localhost:8000/chess/queen'  # Replace with your actual URL

# Send the POST request
response = requests.post(url, json=json_data)

# Print the response content
print(response.text)
