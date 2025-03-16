import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
PARTNER_TOKEN = os.getenv("PARTNER_TOKEN")


BASE_URL= "https://fleet-api.prd.na.vn.cloud.tesla.com"
AUTH_URL = "https://auth.tesla.com/oauth2/v3/authorize"
TOKEN_URL = "https://auth.tesla.com/oauth2/v3/token"
SCOPES = "openid email offline_access vehicle_read fleet:vehicles"