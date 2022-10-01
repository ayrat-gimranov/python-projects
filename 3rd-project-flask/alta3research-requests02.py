#!/usr/bin/env python3

''' Project 3 FLASK for Alta3 Python/Linux class
Author: Ayrat Gimranov'''

# import dependencies
import json
import requests

# define an API url
URL = "http://localhost:2224/"

# a function that retrieves data from database
def get_collection():

    try: # attempt a get request

        # send a GET request to an API server
        response = requests.get(URL + "view")

        # decode JSON response into pythonic data
        response_dc = response.json()

        #if no cars are in database
        if len(response_dc) == 0:
            print("\nCar collection is empty.\n")
        
        #if there are cars in database, display a user friendly message
        else:
            print("\n~~~~~~~~~~~~~~~~~~~~~\n  My Car Collection\n~~~~~~~~~~~~~~~~~~~~~\n")
            for car in response_dc:
                print("YEAR:", car[0])
                print("MAKE:", car[1])
                print("MODEL:", car[2])
                print("---------------------")
            
            print("     End of List\n---------------------\n")

    except: # if GET requests fails, print a message
        print("\n~~~~~ Error fetching the list ~~~~~\n")

# a function that adds data to database
def add_to_collection():

    # initialze empty strings
    year=""
    make=""
    model=""

    # loop until we get the correct year format
    while len(year.strip()) != 4 or not year.strip().isdigit():
        year = input("What is the YEAR of the car? (ex. 1995)\n")
    
    # loop until user types something
    while not make:			
        make = input("What is the MAKE of the car?\n")
    while not model:
        model = input("What is the MODEL of the car?\n")
	
    # combine into a dictionary
    car = {
			"year": int(year),
			"make": make,
			"model": model
			}
            
    car = json.dumps(car) #convert python object into json string
    
    # attemp a POST request to API server
    try:
        # attach json string to our POST request as a required second parameter
        resp = requests.post(f"{URL}add", json=car)
        print("\n~~~~~", resp.text, "~~~~~\n")

    # notify user if POST requests fails
    except:
        print("\n~~~~~ Error saving to database~~~~~\n")
	
# staring point
def main():

    # repeat user actions
	while True:
        # loop until user types one of the given choices
		while True:
			choice = input("Make a choice:\n [1] - View collection of cars\n [2] - Add a new car to collection\n [3] - Quit\n>").strip() # get rid of white spaces
			if choice == '1' or choice == '2' or choice == '3':
				break
			else: # loop again if wrong input
				print('Wrong input. Type 1, 2 or 3 and hit Enter')

        # once we break out of the loop, call a corresponding function
		if choice == '1':
			get_collection()
		elif choice == '2':
			add_to_collection()
		else:
			print("Good bye!")
			break
	
if __name__ == "__main__":
	main()