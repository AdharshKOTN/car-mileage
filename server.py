import os
import requests
from flask import Flask, redirect, request
from urllib.parse import urlencode
from dotenv import load_dotenv
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPES, AUTH_URL, TOKEN_URL

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return '<a href="/login">Login with Tesla</a>'

@app.route("/login")
def login():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": SCOPES
    }
    return redirect(f"{AUTH_URL}?{urlencode(params)}")

@app.route("/callback")
def callback():
    code = request.args.get("code")

    if not code:
        return "No code found in redirect."

    data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }

    response = requests.post(TOKEN_URL, json=data)
    response.raise_for_status()

    token_data = response.json()
    return f"""
    <h3>Access Token:</h3>
    <pre>{token_data['access_token']}</pre>
    <h3>Refresh Token:</h3>
    <pre>{token_data['refresh_token']}</pre>
    """

if __name__ == "__main__":
    app.run(port=5000, debug=True)
