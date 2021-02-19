# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from dotenv import load_dotenv
load_dotenv()
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
flightSearch = FlightSearch()
flightData = FlightData()
data = DataManager()
sheet_data = data.get_data()

for data in sheet_data:
    flightData.get_flight_data(data)
    flightSearch.search_flight(data)
