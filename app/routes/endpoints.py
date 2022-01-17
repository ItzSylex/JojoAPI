from app import app
from app.getter import GetData
from flask import request, jsonify
from flask_cors import CORS, cross_origin

rou = GetData()


@app.route('/', methods=['GET'])
@cross_origin()
def get_all_data():

    if request.args:
        data = rou.valid_query(request.args)
        return jsonify(data)
    else:
        data = rou.get_data(None, None, None)
        a = jsonify(data)
        print(a.headers)
        return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}


@app.route('/StardustCrusaders', methods=['GET'])
@cross_origin()
def get_stardust():
    data = rou.get_data('StardustCrusaders', None, None)
    return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/DiamondIsUnbreakable', methods=['GET'])
@cross_origin()
def get_diamond():
    data = rou.get_data('DiamondIsUnbreakable', None, None)
    return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/GoldenWind', methods=['GET'])
@cross_origin()
def get_golden():
    data = rou.get_data('GoldenWind', None, None)
    return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}
