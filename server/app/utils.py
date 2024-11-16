from datetime import datetime, timedelta

def get_expiration_date(expires_in):
  date = datetime.now() + timedelta(seconds=expires_in)
  return date.isoformat()

def is_expired(date_str):
  return datetime.fromisoformat(date_str) < datetime.now()