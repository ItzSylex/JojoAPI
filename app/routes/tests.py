from app import app
from flask import request, jsonify


@app.route('/test', methods = ['GET'])
def test():
   test_dict = {"Key1": "Value1", "Key2": ["Value2","Value2","Value2",]}
   print(jsonify(test_dict).headers)
   return jsonify(test_dict)
