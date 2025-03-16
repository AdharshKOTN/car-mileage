import requests
import json
from config import PARTNER_TOKEN, BASE_URL


url = BASE_URL + '/api/1/partner_accounts'
headers = {
    "Authorization": f"Bearer {PARTNER_TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "domain": "http://localhost:5000"
}

print(f"DEBUG: url -- {url}")

response = requests.post(url, headers=headers, data=json.dumps(data))

print("Status Code:", response.status_code)
print("Response:", response.json())
