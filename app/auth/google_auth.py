import requests
import time

TOKEN_URL = "https://oauth2.googleapis.com/token"

class GoogleAuth:
    def __init__(self, client_id, client_secret, refresh_token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.access_token = None
        self.expiry = 0

    def get_access_token(self):
        if self.access_token and time.time() < self.expiry:
            return self.access_token

        response = requests.post(TOKEN_URL, data={
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
            "grant_type": "refresh_token"
        })

        data = response.json()

        if "access_token" not in data:
            raise Exception(f"Token refresh failed: {data}")

        self.access_token = data["access_token"]
        self.expiry = time.time() + data.get("expires_in", 3600) - 60

        return self.access_token
