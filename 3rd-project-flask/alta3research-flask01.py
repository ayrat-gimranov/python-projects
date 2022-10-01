#!/usr/bin/env python3

''' Project 3 FLASK for Alta3 Python/Linux class
Author: Ayrat Gimranov'''

# import dependencies
from flask import Flask
from flask import request
from flask import jsonify
import sqlite3
import json

# initiate FLASK
app = Flask(__name__)

# use a decorator to call view_all() function when /view route gets hit with a GET request
@app.route("/view")
def view_all():
    # get the car list from a database
	with sqlite3.connect('cars.db') as conn: # open connection
		cur = conn.cursor() # create cursor object to perform operations on a table
		res = cur.execute("SELECT * from cars")
		res = res.fetchall() # grab all rows from table

	# return the list as json
	return jsonify(res)

# use a decorator to call add_to_collection() function when /add route gets hit with a POST request
@app.route("/add", methods=["POST"])
def add_to_collection():
    # extract json data
	data = request.json

	#convert json string into pythonic data
	data = json.loads(data) 

	#use a getter to extract the data from an object, if it's there 
	year = data.get('year')
	make = data.get('make')
	model = data.get('model')

	# attempt connecting to cars database
	try:
		with sqlite3.connect('cars.db') as conn:
			cur = conn.cursor()

			# add new data into a table
			cur.execute("INSERT INTO cars (year, make, model) VALUES (?,?,?)", (year,make,model))

			# commit the changes to a DB table
			conn.commit()	

		return "Car added to database"
	# if DB operation fails
	except:
		return "Unable to add to DB"


if __name__ == "__main__":
	# entry point
	# attempt connecting to DB and creating a table, unless exists already
	try:		
		conn = sqlite3.connect('cars.db')
		# create a table using a schema
		conn.execute('''CREATE TABLE IF NOT EXISTS cars
		(YEAR           INT    NOT NULL,
		MAKE           TEXT     NOT NULL,
		MODEL          TEXT);''')
		print("connected to DB")

		#close connection to DB
		conn.close()
	#if DB connection fails
	except:
		print("error connecting to DB")
    
	# start listening for requests
	app.run(host="0.0.0.0", port=2224)


