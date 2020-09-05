from flask import Flask

app = Flask(__name__)

from app.routes import endpoints
from app.routes import error
