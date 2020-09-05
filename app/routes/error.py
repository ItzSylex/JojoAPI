from app import app
from flask import request, jsonify



@app.errorhandler(404)
def not_found(error):
    """Page not found."""
    return {"message": 'This page does not exist'}, 404

@app.errorhandler(400)
def bad_request(error):
    """Bad request."""
    return {'message': 'Bad request'}, 400

@app.errorhandler(500)
def server_error(error):
    """Internal server error."""
    return {"message": 'Internal server error'}, 500
