from flask import Flask
import hashlib, secrets

def create_app():
  app = Flask(__name__)
  app.secret_key = hashlib.sha256(secrets.token_bytes(16)).hexdigest()

  # Setup api routes
  from .routes import api
  app.register_blueprint(api)

  # Setup database
  from .database import init_db, close_db
  app.teardown_appcontext(close_db)
  with app.app_context():
    init_db()

  return app
