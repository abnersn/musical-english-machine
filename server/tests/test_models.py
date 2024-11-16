import pytest, sqlite3

@pytest.fixture
def in_memory_db():
  connection = sqlite3.connect(':memory:')
  cursor = connection.cursor()

  # Create db schema
  with open('schema.sql') as f:
    cursor.execute(f.read())
    connection.commit()

  # Yield connection to the test
  yield connection

  # Clean up after the test
  connection.close()

def test_get_user(mocker):
  