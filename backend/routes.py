import flask
import json
from flask import request, jsonify, Blueprint

simple_page = Blueprint('simple_page', __name__,)

with open('./tournaments.json') as f:
  tournaments = json.load(f)

@simple_page.route('/', methods=['GET'])
def home():
    return "<h1>Some weird html here.</h1>"

@simple_page.route('/api/tournaments/all', methods=['GET'])
def getAll():
    return jsonify(tournaments)

# get by id query params way
@simple_page.route('/api/tournaments', methods=['GET'])
def get_by_id1():
    if '_id' in request.args:
        id = int(request.args['_id'])
    else:
        return 'No id provided'
    
    for book in tournaments:
        if book['_id'] == id:
            return jsonify(book)
    return 'No tournament found for id '+id

# get by id path variable way
@simple_page.route('/api/tournaments/<id>', methods=['GET'])
def get_by_id2(id):
    if id:
        id = str(id)
    else:
        return 'No id provided'
    
    for book in tournaments:
        if book['_id'] == id:
            return jsonify(book)
    return 'No tournament found for id '+str(id)
