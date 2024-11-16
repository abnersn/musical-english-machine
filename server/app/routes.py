from os import environ

from flask import Blueprint, request, redirect
from urllib.parse import urlencode
import hashlib, secrets

api = Blueprint('api', __name__, url_prefix='/api')

# Generate string to validate requests
api_state = hashlib.sha256(secrets.token_bytes(16)).hexdigest()

@api.route("/")
def main():
  return "<p>Hello, world!</p>"

@api.route("/authorize")
def authorize():
  data = urlencode({
    "response_type": 'code',
    "client_id": environ.get("SPOTIFY_CLIENT_ID"),
    "scope": "user-read-recently-played",
    "redirect_uri": "http://localhost/api/callback",
    "state": api_state
  })
  return redirect(f'https://accounts.spotify.com/authorize?{data}')

@api.route("/callback", methods=["GET"])
def callback():
  if (request.args.get("state") != api_state):
    return "Invalid request", 500

  if (request.args.get("error") == "access_denied"):
    return "User did not authorize", 500

  return f"<h1>Hello spotify {request.args.get("code")}</h1>"
