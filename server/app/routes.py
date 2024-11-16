from os import environ

from flask import Blueprint
from flask import current_app, request, redirect
from urllib.parse import urlencode

from .models import user_auth_flow

api = Blueprint('api', __name__, url_prefix='/api')

@api.route("/authorize")
def authorize():
  data = urlencode({
    "response_type": 'code',
    "client_id": environ.get("SPOTIFY_CLIENT_ID"),
    "scope": "user-read-recently-played",
    "redirect_uri": f"{environ.get("APP_URI")}/api/callback",
    "state": current_app.secret_key
  })
  return redirect(f'https://accounts.spotify.com/authorize?{data}')

@api.route("/callback", methods=["GET"])
def callback():
  if (request.args.get("state") != current_app.secret_key):
    return "Invalid request", 500

  if (request.args.get("error") == "access_denied"):
    return "User did not authorize", 500

  user = user_auth_flow(request.args.get("code"))
  return redirect(f'/?token_request_code={user['token_request_code']}')
