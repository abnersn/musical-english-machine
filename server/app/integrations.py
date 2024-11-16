from os import environ
from .utils import get_expiration_date
import requests

def get_spotify_user_token(token_request_code):
  auth_response = requests.post('https://accounts.spotify.com/api/token', data={
    'code': token_request_code,
    'redirect_url': f"{environ.get("APP_URI")}/api/callback",
    'grant_type': 'authorization_code'
  })
  user_data = auth_response.json()

  return {
    'token_request_code': token_request_code,
    'access_token': user_data['access_token'],
    'expiration_date': get_expiration_date(user_data['expires_in']),
    'refresh_token': user_data['refresh_token']
  }

def refresh_spotify_user_token(user):
  auth_response = requests.post('https://accounts.spotify.com/api/token', data={
    'client_id': environ.get("SPOTIFY_CLIENT_ID"),
    'refresh_token': user["refresh_token"],
    'grant_type': 'refresh_token'
  })
  user_data = auth_response.json()
  access_token = user_data['access_token']
  expiration_date = user_data['expires_in']

  return access_token, expiration_date
