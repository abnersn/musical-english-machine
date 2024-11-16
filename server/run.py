from os import environ
from flask_socketio import SocketIO
from app import create_app
from dotenv import load_dotenv

load_dotenv()

app = create_app()
socketio = SocketIO(app)

if __name__ == "__main__":
  socketio.run(app,
    debug=environ.get('DEBUG') == '1',
    host=environ.get('HOST'),
    port=environ.get('PORT')
  )