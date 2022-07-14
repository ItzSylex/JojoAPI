from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config["DEBUG"] = True
CORS(app)
from app.routes import endpoints
from app.routes import error
