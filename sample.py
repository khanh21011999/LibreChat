import json
import requests

# API key
api_key = "959f5d266a79e310d9b77c597188f701734f0a4ea156b23522f545716530e4c7"

# API endpoint
url = "https://api.together.xyz/v1/models"

# headers
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# make request
response = requests.get(url, headers=headers)

# print the response status code
print(f"Response status code: {response.status_code}")

# parse JSON response
data = response.json()

# print the JSON response
print("JSON Response:")
print(json.dumps(data, indent=2))

# extract an ordered list of unique model IDs
model_ids = sorted(
    [
        model['id']
        for model in data
        if model['type'] == 'chat'
    ]
)

# print the model IDs
print("\nModel IDs:")
print(model_ids)

# write result to a text file
with open("models_togetherai.json", "w") as file:
    json.dump(model_ids, file, indent=2)

# print a success message
print("\nModel IDs written to models_togetherai.json file successfully.")
