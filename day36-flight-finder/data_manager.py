import requests
from pprint import pprint
sheety_endpoint = "https://api.sheety.co/f492e1855f19e899b480867a62983303/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.sheety_response = requests.get(url=sheety_endpoint)
        self.sheet_data = self.sheety_response.json()
        pprint(self.sheet_data)

    def get_data(self):
        return self.sheet_data["prices"]
