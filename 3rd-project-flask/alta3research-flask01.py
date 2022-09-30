#!/usr/bin/env python3

from crypt import methods
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

import json

app = Flask(__name__)

car_collection= []

@app.route("/view")
def view_all():
	# get the car list from a database
	# return the list as json

	return jsonify(car_collection)

@app.route("/add", methods=["POST"])
def add_to_collection():
	# extract json data
	data = request.json
	data = json.loads(data)	
	car_collection.append(data)

	return jsonify(car_collection)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=2224)