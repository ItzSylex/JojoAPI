from flask import Flask, jsonify, request
import json
from getter import GetData

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

rou = GetData()


@app.route('/', methods=['GET'])
def get_all_data():

    if request.args:
        data = rou.valid_query(request.args)
        return jsonify(data)
    else:
        data = rou.get_data(None, None, None)
        return jsonify(data), 200


@app.route('/StardustCrusaders', methods=['GET'])
def get_stardust():
    data = rou.get_data('StardustCrusaders', None, None)
    return jsonify(data), 200

@app.route('/DiamondIsUnbreakable', methods=['GET'])
def get_diamond():
    data = rou.get_data('DiamondIsUnbreakable', None, None)
    return jsonify(data), 200

@app.route('/GoldenWind', methods=['GET'])
def get_golden():
    data = rou.get_data('GoldenWind', None, None)
    return jsonify(data), 200


" === Error Handling === "

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

if __name__ == '__main__':
    app.run(debug = True)
