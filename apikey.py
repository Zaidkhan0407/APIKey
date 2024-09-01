import requests

# Random API key (for demo purposes only)
api_key = '1234567890abcdef'

# Example API endpoint (random joke API for demonstration)
url = 'https://httpbin.org/anything'

# Set up headers with API key and content type
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Make a GET request to the API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # If successful, print the data received from the API
    print('Response:', response.json())
else:
    # If unsuccessful, print an error message and the status code
    print(f'Error! Status code: {response.status_code}')
