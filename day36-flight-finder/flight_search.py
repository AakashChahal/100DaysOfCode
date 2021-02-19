import requests
from flight_data import HEADERS
tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:
    def __init__(self):
        self.parameters = {}
        self.response = None

    def search_flight(self, data):
        self.parameters = {
            "fly_from": "DEL",
            "fly_to": data["iataCode"],
            "dateFrom": "20/02/2021",
            "dateTo": "22/08/2021",
            "curr": "INR"
        }
        self.response = requests.get(url=tequila_endpoint, params=self.parameters, headers=HEADERS)
        # print(response.json().keys())
        # print(self.response)
        print(f"{data['city']}: ₹{self.response.json()['data'][0]['price']}")
