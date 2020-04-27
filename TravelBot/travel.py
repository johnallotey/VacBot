from amadeus import Client, ResponseError
import logging
import flask
import requests
import json
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

logger = logging.getLogger('your_logger')
logger.setLevel(logging.DEBUG)

amadeus = Client(
    client_id='','',
    log_level='debug'
)

@app.route('/destination/<origin>', methods=['GET'])
def get_flight(origin):
# Flight Inspiration Search
	r = amadeus.shopping.flight_destinations.get(origin='MAD')
	#json_data = json.loads(r)
	#print(r.result)
	return jsonify(r.result)
    
"""
are you keeping the commented out code below or deleting it?
"""
#@app.route('/snap_info', methods=['GET'])
#def home():
   # return jsonify(get_info())

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify("John")
app.run() 
