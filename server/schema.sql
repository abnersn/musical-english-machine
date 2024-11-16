CREATE TABLE IF NOT EXISTS users (
  token_request_code TEXT PRIMARY KEY NOT NULL,
  expiration_date TEXT NOT NULL,
  access_token TEXT,
  refresh_token TEXT
)