import requests



import numpy
import scipy
import dash
import seaborn
import matplotlib
import json


#https://developers.skyscanner.net/docs/flights-live-prices/overview



#curl --request POST 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create' --header 'x-api-key: your-api-key' --data ' {"query":{"market":"UK","locale":"en-GB","currency":"GBP","query_legs":[{"origin_place_id":{"iata":"LHR"},"destination_place_id":{"iata":"SIN"},"date":{"year":2025,"month":04,"day":11}}],"adults":1}}'


# Define the API URL
url = "https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create"

# Your API Key
api_key = "your-api-key"

# Headers
headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json"
}

# Data Payload
data = {
    "query": {
        "market": "UK",
        "locale": "en-GB",
        "currency": "GBP",
        "query_legs": [
            {
                "origin_place_id": {"iata": "LHR"},
                "destination_place_id": {"iata": "SIN"},
                "date": {"year": 2025, "month": 4, "day": 11}
            }
        ],
        "adults": 1
    }
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)


if response.status_code == 200:
    response_json = response.json()
    
    # Extract session ID (modify the key based on the actual response structure)
    session_id = response_json.get("session_id", "No session ID found")

    print("Session ID:", session_id)
else:
    print("Error:", response.status_code, response.text)

# Print the response




#GET SESSSION TOKEN AUTOMATICALLY
curl --location --request POST 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/poll/SESSION_TOKEN' --header 'x-api-key: your-api-key'

data= requests.get('https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create')

json_data = {
{
  "itineraryId": "string"
}}
