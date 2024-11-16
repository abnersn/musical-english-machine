from datetime import datetime, timedelta

def get_expiration_date(expires_in):
  return datetime.now() + timedelta(seconds=expires_in)

def is_expired(date_str):
  return datetime.strptime(date_str) < datetime.now()