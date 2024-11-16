from os import environ
import requests
from app.database import get_db
from datetime import datetime, timedelta

def user_auth_flow(token_request_code):
  # First we try to get data from existing user
  db = get_db()
  cursor = db.cursor()
  cursor.execute(
    "SELECT * FROM users WHERE token_request_code = ?",
    (token_request_code,)
  )
  user = cursor.fetchone()
  
  # If it doesn't exist, we request access token to create it
  if user is None:
    auth_response = requests.post('https://accounts.spotify.com/api/token', data={
      'code': token_request_code,
      'redirect_url': f"{environ.get("APP_URI")}/api/callback",
      'grant_type': 'authorization_code'
    })
    user_data = auth_response.json()

    user = {
      'token_request_code': token_request_code,
      'access_token': user_data['access_token'],
      'expiration_date': datetime.now() + timedelta(seconds=user_data['expires_in']),
      'refresh_token': user_data['refresh_token']
    }

    db.execute('''
      INSERT INTO users (
        token_request_code,
        access_token,
        expiration_date,
        refresh_token
      )
    ''', tuple(user.values()))
  
  # If user exists, but token is expired, we request a new one
  if datetime.strptime(user["expiration_date"]) < datetime.now():
    auth_response = requests.post('https://accounts.spotify.com/api/token', data={
      'client_id': environ.get("SPOTIFY_CLIENT_ID"),
      'refresh_token': user["refresh_token"],
      'grant_type': 'refresh_token'
    })
    user_data = auth_response.json()
    user['access_token'] = user_data['access_token']
    user['expiration-date'] = datetime.now() + timedelta(seconds=user_data['expires_in'])

    db.execute('''
      UPDATE users SET
        access_token = ?,
        expiration_date = ?
      WHERE
        id = ?
    ''', (
      user['access_token'],
      user['expiration-date'],
      token_request_code
    ))
  
  return user