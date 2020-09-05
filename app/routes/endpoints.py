from app import app
from app.getter import GetData
from flask import request, jsonify

rou = GetData()

# @app.route('/', defaults={'serie': None})
# @app.route('/<serie>')
# def endpoint(serie = None):
#
#     valid_serie = [
#         'DiamondIsUnbreakable',
#         'GoldenWind',
#         'StardustCrusaders'
#     ]
#
#     if serie is not None and not request.args:
#         data = rou.get_data(None, None, None)
#         return jsonify(data), 200
#
#     if serie and request.args:
#         if serie in valid_serie:
#
#             data = rou.get_data(serie, None, None)


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
