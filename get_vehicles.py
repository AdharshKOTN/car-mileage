import requests
from config import ACCESS_TOKEN, BASE_URL

url = BASE_URL + 'api/1/vehicles'
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    vehicles = response.json()
    print("Vehicles:", vehicles)
else:
    print(f"Error {response.status_code}: {response.text}")