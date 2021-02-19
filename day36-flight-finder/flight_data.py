import requests
HEADERS = {
            "apikey": "EPJEbACajU0tuaul2TLsDtADLiWF6JUB"
        }
flight_search_endpoint = "https://tequila-api.kiwi.com/locations/query"


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_parameters = {}
        self.update_parameters = {}
        self.update_endpoint = ""

    def get_flight_data(self, data):
        self.update_endpoint = f"https://api.sheety.co/f492e1855f19e899b480867a62983303/flightDeals/prices/{data['id']}"
        self.flight_parameters = {
            "term": data["city"]
        }
        # print("middle")
        updated_data = requests.get(url=flight_search_endpoint, params=self.flight_parameters, headers=HEADERS)
        loc_data = updated_data.json()["locations"][0]
        self.update_parameters = {
            "price": {
                "iataCode": loc_data['code']
            }
        }
        requests.put(url=self.update_endpoint, json=self.update_parameters)
