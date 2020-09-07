from flask import Flask

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config["DEBUG"] = True

from app.routes import endpoints
from app.routes import error
from app.routes import tests
