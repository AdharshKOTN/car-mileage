import requests
import json
import os
from config import CLIENT_ID, CLIENT_SECRET, BASE_URL

PARTNER_AUTH_URL = "https://fleet-auth.prd.vn.cloud.tesla.com/oauth2/v3/token"

payload = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "scope": "openid vehicle_device_data vehicle_cmds vehicle_charging_cmds",
    "audience" : BASE_URL
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(PARTNER_AUTH_URL, headers=headers, json=payload)

if response.status_code != 200:
    print("❌ Failed to get partner token")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
    exit()

partner_token = response.json().get("access_token")
print("✅ Partner token acquired:", partner_token)
