import pytest, sqlite3
from datetime import datetime
from unittest.mock import patch

from app import models

@pytest.fixture
def in_memory_db():
  connection = sqlite3.connect(':memory:')
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()

  # Create db schema
  with open('schema.sql') as f:
    cursor.execute(f.read())
    connection.commit()

  # Yield connection to the test
  yield connection

  # Clean up after the test
  connection.close()

@patch('app.models.get_db')
def test_get_user(mock_db, in_memory_db):
  mock_db.return_value = in_memory_db

  # Users are created
  with patch('app.models.get_spotify_user_token') as mock_get_spotify_user_token:
    mock_get_spotify_user_token.return_value = {
      'token_request_code': '123',
      'access_token': '456',
      'expiration_date': datetime.now().isoformat(),
      'refresh_token': '789'
    }
    models.user_auth_flow('123')
    cursor = in_memory_db.cursor()
    cursor.execute('''
      SELECT
        *
      FROM
        users
      WHERE
        token_request_code="123"
    ''')
    user = cursor.fetchone()
    assert user['access_token'] == '456'

  with patch('app.models.refresh_spotify_user_token') as mock_get_spotify_user_token:
    mock_get_spotify_user_token.return_value = ['321', datetime.now().isoformat()]
    models.user_auth_flow('123')
    cursor = in_memory_db.cursor()
    cursor.execute('''
      SELECT
        *
      FROM
        users
      WHERE
        token_request_code="123"
    ''')
    user = cursor.fetchone()
    assert user['access_token'] == '321'