from os import environ
from .utils import get_expiration_date, encode_base64
from .exceptions import SpotifyAPIError
import requests

def create_spotify_user_token(token_request_code):
  authorization = ':'.join([
    environ.get('SPOTIFY_CLIENT_ID'),
    environ.get('SPOTIFY_CLIENT_SECRET')
  ])

  auth_response = requests.post('https://accounts.spotify.com/api/token', data={
    'code': token_request_code,
    'redirect_uri': f"{environ.get("APP_URI")}/api/callback",
    'grant_type': 'authorization_code'
  }, headers={
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f"Basic {encode_base64(authorization)}"
  })

  response_data = auth_response.json()
  if ('error' in response_data):
    raise SpotifyAPIError(
      response_data['error_description']
    )

  return {
    'token_request_code': token_request_code,
    'access_token': response_data['access_token'],
    'expiration_date': get_expiration_date(response_data['expires_in']),
    'refresh_token': response_data['refresh_token']
  }

def refresh_spotify_user_token(user):
  authorization = ':'.join([
    environ.get('SPOTIFY_CLIENT_ID'),
    environ.get('SPOTIFY_CLIENT_SECRET')
  ])

  auth_response = requests.post('https://accounts.spotify.com/api/token', data={
    'client_id': environ.get("SPOTIFY_CLIENT_ID"),
    'refresh_token': user["refresh_token"],
    'grant_type': 'refresh_token'
  }, headers={
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f"Basic {encode_base64(authorization)}"
  })

  response_data = auth_response.json()
  if ('error' in response_data):
    raise SpotifyAPIError(
      response_data['error_description']
    )

  access_token = response_data['access_token']
  expiration_date = response_data['expires_in']

  return access_token, expiration_date
