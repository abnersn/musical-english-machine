from flask import Flask
import app.routes as routes

app = Flask(__name__)
app.register_blueprint(routes.api)
