from .database import get_db
from .utils import is_expired
from .integrations import create_spotify_user_token, refresh_spotify_user_token

def user_auth_flow(token_request_code):
  # First we try to get data from existing user
  db = get_db()
  cursor = db.cursor()
  cursor.execute(
    "SELECT * FROM users WHERE token_request_code = ?",
    (token_request_code,)
  )
  user = cursor.fetchone()
  
  # If user doesn't exist on db, we request access token 
  if user is None:
    user = create_spotify_user_token(token_request_code)
    db.execute('''
      INSERT INTO users (
        token_request_code,
        access_token,
        expiration_date,
        refresh_token
      ) VALUES (?, ?, ?, ?)
    ''', tuple(user.values()))
    return user
  
  # If user exists on db, but token is expired, we request a new one
  if is_expired(user["expiration_date"]):
    access_token, expiration_date = refresh_spotify_user_token(user)
    db.execute('''
      UPDATE users SET
        access_token = ?,
        expiration_date = ?
      WHERE
        token_request_code = ?
    ''', (
      access_token,
      expiration_date,
      token_request_code
    ))
  
  return user