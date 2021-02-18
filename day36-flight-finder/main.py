# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from dotenv import load_dotenv
load_dotenv()
import requests
from pprint import pprint

sheety_endpoint = "https://api.sheety.co/f492e1855f19e899b480867a62983303/flightDeals/prices"
sheety_response = requests.get(url=sheety_endpoint)
sheet_data = sheety_response.json()["prices"]
print(sheet_data)







# tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"
#
# header = {
#     "apikey": "EPJEbACajU0tuaul2TLsDtADLiWF6JUB"
# }
# parameters = {
#     "fly_from": "DEL",
#     "fly_to": "BHX",
#     "dateFrom": "18/02/2021",
#     "dateTo": "18/08/2021",
#     "currency": "INR"
# }
# response = requests.get(url=tequila_endpoint, params=parameters, headers=header)
# # print(response.json().keys())
# print(response.json()["fx_rate"])
