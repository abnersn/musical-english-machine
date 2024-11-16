from datetime import datetime, timedelta
from base64 import b64encode

def get_expiration_date(expires_in):
  date = datetime.now() + timedelta(seconds=expires_in)
  return date.isoformat()

def is_expired(date_str):
  return datetime.fromisoformat(date_str) < datetime.now()

def encode_base64(string):
  return b64encode(string.encode('utf-8')).decode('utf-8')