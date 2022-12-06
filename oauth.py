import json

import requests


def get_new_api_key():
    with open("credentials.json") as f:
        credentials = json.load(f)
        client_id = credentials["client_id"]
        client_secret = credentials["client_secret"]
    grant_type = "client_credentials"

    # Build the API request URL
    api_url = "https://oauth.battle.net/token"

    # Set the request headers
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    # Set the request body
    body = {"client_id": client_id, "client_secret": client_secret,
            "grant_type": grant_type}

    # Send the request to the API
    response = requests.post(api_url, headers=headers, data=body)

    # Check the response status code
    if response.status_code != 200:
        print("API request failed with status code:", response.status_code)
        with open('error.txt', 'w') as f:
            f.write(response.text)
    else:
        # Parse the response JSON
        response_json = response.json()
        # Extract the access token from the response
        access_token = response_json["access_token"]
        return access_token
