from dotenv import load_dotenv
load_dotenv()
import requests
from datetime import datetime
import os

DATE = datetime.now().date().strftime("%d/%m/%Y")
TIME = datetime.now().time().strftime("%H:%M:%S")
# print(DATE)
# print(TIME)
GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 172
AGE = 20

APP_ID = os.getenv("APP_ID")
API_key = os.getenv("API_key")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercise you did: ")
exercise_data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg":  str(WEIGHT_KG),
    "height_cm": str(HEIGHT_CM),
    "age": str(AGE)
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_key
}

header_sheety = {
    "Authorization": os.getenv("sheety_authorization")
}

nutrionix_response = requests.post(url=exercise_endpoint, json=exercise_data, headers=headers)
data = nutrionix_response.json()["exercises"]
# print(data)
sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
for result in data:
    workout_data = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": result['name'].title(),
            "duration": str(result['duration_min']).replace('min', ''),
            "calories": result["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=workout_data, headers=header_sheety)
    print(sheety_response.text)
