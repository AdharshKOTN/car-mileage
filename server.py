import os
import requests
from flask import Flask, redirect, request
from urllib.parse import urlencode, quote
from dotenv import load_dotenv
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPES, AUTH_URL, TOKEN_URL

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return '<a href="/login">Login with Tesla</a>'

@app.route("/login")
def login():
    encoded_scope = quote(SCOPES)
    print(f"DEBUG: encoded_scope - {encoded_scope}")
    
    params = [
    ("client_id", CLIENT_ID),
    ("redirect_uri", REDIRECT_URI),
    ("response_type", "code"),
    ("prompt", "login"),
    ("locale", "en-US"),
    ("state", "randomstring123"),
]
    encoded_params = urlencode(params)
    print(f"DEBUG: encoded params {encoded_params}")
    full_url = f"{AUTH_URL}?{encoded_params}&scope={encoded_scope}"
    print(f"DEBUG: full-url {full_url}")
    # return full_url
    return redirect(full_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")

    if not code:
        return "No authorization code received.", 400

    data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(TOKEN_URL, json=data, headers=headers)

    if response.status_code != 200:
        return f"Token exchange failed: {response.text}", response.status_code

    token_data = response.json()

    access_token = token_data.get("access_token")
    refresh_token = token_data.get("refresh_token")
    expires_in = token_data.get("expires_in")

    # Show tokens for now (secure this later!)
    return f"""
    <h2>Access Token:</h2>
    <pre>{access_token}</pre>
    <h2>Refresh Token:</h2>
    <pre>{refresh_token}</pre>
    <h2>Expires In:</h2>
    <pre>{expires_in} seconds</pre>
    """

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
