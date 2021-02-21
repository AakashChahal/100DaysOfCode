import requests
from flight_data import HEADERS
from datetime import datetime, timedelta
from notification_manager import NotificationManager
notifier = NotificationManager()
tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:
    def __init__(self):
        self.parameters = {}
        self.date_from = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        self.date_to = (datetime.now() + timedelta(days=(6 * 30))).strftime("%d/%m/%Y")
        self.sms = None
        self.response = None

    def search_flight(self, data):
        self.parameters = {
            "fly_from": "DEL",
            "fly_to": data["iataCode"],
            "dateFrom": self.date_from,
            "dateTo": self.date_to,
            "max_fly_duration": 20,
            "curr": "INR"
        }
        # print(self.date)
        self.response = requests.get(url=tequila_endpoint, params=self.parameters, headers=HEADERS)
        # print(response.json().keys())
        # print(self.response)
        flight_price = self.response.json()['data'][0]['price']
        if flight_price <= data['lowestPrice']:
            self.sms = f"""{data['city']}: ₹{flight_price}
            Booking link: {self.response.json()['data'][0]['deep_link']}"""
            notifier.send_sms(self.sms)
