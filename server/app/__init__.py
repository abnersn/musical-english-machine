from os import environ

from flask import Flask
from flask import redirect
from urllib.parse import urlencode
import hashlib, secrets

app = Flask(__name__)

@app.route("/api")
def main():
  return "<p>Hello, world!</p>"

@app.route("/api/authorize")
def authorize():
  state = hashlib.sha256(secrets.token_bytes(16)).hexdigest()
  data = urlencode({
    "response_type": 'code',
    "client_id": environ.get("SPOTIFY_CLIENT_ID"),
    "scope": "user-read-recently-played",
    "redirect_uri": "http://localhost",
    "state": state
  })
  return redirect(f'https://accounts.spotify.com/authorize?{data}')
