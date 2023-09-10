import requests
import json
import numpy as np

# Generate random numeric data 
random_data = np.random.rand(10).tolist()
data = {"features": random_data}

headers = {"Content-Type": "application/json"}

# Make the POST request
response = requests.post("http://localhost:5000/predict", json=data, headers=headers)

# Handle the response 
if response.status_code == 200:
    result = response.json()
    predictions = result.get("predictions")
    if predictions is not None:
        print("Predictions:", predictions)
    else:
        print("No predictions in the response.")
else:
    print("Error:", response.status_code, response.text)


