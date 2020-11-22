from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
#from rasa_sdk import Tracker
from rasa_sdk.events import AllSlotsReset, Restarted
#from email.message import EmailMessage
import json
from email_config import Config
from flask_mail_check import send_email
from zomato_slots import results

import zomatopy
import json
DEFAULT_DATA_PATH = "data"
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"6f74761b3897ce54af930b2538276c97"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'Chinese':5,'Mexican':25,'Italian':30,'American':55,'South Indian':7,'North Indian':50}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

class SendMail(Action):
	def name(self):
		return 'action_send_email'
		
	def run(self, dispatcher, tracker, domain):
		global restaurants
		recipient = tracker.get_slot('email')
		print(recipient)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		restaurants = results(loc,cuisine,price)
		top10 = restaurants.head(10)
		print("got this correct email is {}".format(recipient))
		send_email(recipient, top10)

		dispatcher.utter_message("Have a great day!")
		
class ActionValidateLocation(Action):
    def name(self):
        return "action_location_valid"

    def run(self, dispatcher, tracker, domain):

        location = tracker.get_slot("location")
        location_validity = "valid"

        if not location:
            location_validity = "invalid"
        else:
            filepath = DEFAULT_DATA_PATH + "/cities.json"

            with open(filepath) as cities_file:

                data = json.load(cities_file)

                if data is not None:
                    tier1_cities = data["data"]["tier1"]
                    tier2_cities = data["data"]["tier2"]

                    tier1_cities_lower = [city.lower() for city in tier1_cities]
                    tier2_cities_lower = [city.lower() for city in tier2_cities]

                    location_validity = (
                        "invalid"
                        if location.lower() not in tier1_cities_lower
                        and location.lower() not in tier2_cities_lower
                        else "valid"
                    )
                else:
                    location_validity = "invalid"

        return [SlotSet("location_validity", location_validity)]


""" Custom action to validate input cuisine
"""
class ActionValidateCuisine(Action):
    def name(self):
        return "action_cuisine_valid"

    def run(self, dispatcher, tracker, domain):

        cuisine = tracker.get_slot("cuisine")
        cuisine_validity = "valid"

        if not cuisine:
            cuisine_validity = "invalid"
        else:
            supported_cuisines = [
                "american",
                "chinese",
                "italian",
                "mexican",
                "north indian",
                "south indian",
            ]

            cuisine_validity = (
                "invalid" if cuisine.lower() not in supported_cuisines else "valid"
            )

        return [SlotSet("cuisine_validity", cuisine_validity)]


class ActionRestarted(Action): 	
	def name(self):
		return 'action_restart'

	def run(self, dispatcher, tracker, domain):
		return[Restarted()] 


class ActionSlotReset(Action): 
	def name(self): 
		return 'action_slot_reset' 

	def run(self, dispatcher, tracker, domain): 
		return[AllSlotsReset()]
