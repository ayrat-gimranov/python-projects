#!/usr/bin/env python3
import json
import re
import requests
import pprint

URL = "http://localhost:2224/"

def get_collection():
	response = requests.get(URL + "view")
	response_dc = response.json()

	if len(response_dc) == 0:
		print("\nCar collection is empty.\n")
	for car in response_dc:
		print()
		pprint.pprint(car)
		print()

def add_to_collection():
	year=""
	make=""
	model=""

	while len(year.strip()) != 4 or not year.strip().isdigit():
		year = input("What is the YEAR of the car? (ex. 1995)\n")
	while not make:			
		make = input("What is the MAKE of the car?\n")
	while not model:
		model = input("What is the MODEL of the car?\n")
	
	car = {
			"year": int(year),
			"make": make,
			"model": model
			}
	
	car = json.dumps(car) #convert python object into json string

	resp = requests.post(f"{URL}add", json=car)
	

def main():
	while True:
		while True:
			choice = input("Make a choice:\n [1] - View collection of cars\n [2] - Add a new car to collection\n [3] - Quit\n>").strip()
			if choice == '1' or choice == '2' or choice == '3':
				break
			else:
				print('Wrong input. Type 1, 2 or 3 and hit Enter')

		if choice == '1':
			get_collection()
		elif choice == '2':
			add_to_collection()
		else:
			print("Good bye!")
			break
	
if __name__ == "__main__":
	main()