from os import getenv
from flask import Flask, request, jsonify
from flask_cors import CORS
import repo
from bson.objectid import ObjectId
import json

app = Flask(__name__)
if getenv('FLASK_ENV') == 'development':
    CORS(app)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def bsonToJSONString(doc):
    return JSONEncoder().encode(doc)


@app.route('/debt/<address>', methods=['GET'])
def getDebt(address):
    result = []
    debts = repo.getAllDebt(address)
    for debt in debts:
        result.append(
            {'address': debt['address'], 'tx': debt['tx'], 'amount': debt['amount']})
    return jsonify(result)


@app.route('/debt/<tx>', methods=['DELETE'])
def deleteDebt(tx):
    repo.deleteOneDebt(tx)
    return {'status': 'OK'}


@app.route('/debt', methods=['POST'])
def addDebt():
    body = request.get_json()
    repo.addDebt(body['address'], body['tx'], body['amount'])
    return {'status': 'OK'}
