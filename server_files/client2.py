import requests
import json

# URL of the Flask server
url = 'https://clamo.serveo.net/upload'  # Replace with your server's URL

# Sample array data
sample_array = [1, 2, 3, 4, 5]

# Convert the array to JSON
payload = json.dumps(sample_array)

# Set the content type header to application/json
headers = {'Content-Type': 'application/json'}

# Send a POST request to the server
response = requests.post(url, data=payload, headers=headers)

# Print the response
data = json.loads(response.content.decode('utf-8'))

print(round(data["result"][0][0],2))

