import requests
from twilio.rest import Client

account_sid = 'AC85c6bf4283fa45de568f6424d8fa0fc7'
auth_token = '<your twilio auth token>'
client = Client(account_sid, auth_token)
api_key = "<your OWM API key>"
my_lon = 77.2167
my_lat = 28.6667
end_point = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": my_lat,
    "lon": my_lon,
    "units": "metric",
    "exclude": "daily,minutely,current,alerts",
    "appid": api_key,
}

response = requests.get(end_point, params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"][0:12]
will_rain = False
for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # print("bring an umbrella")
    message = client.messages.create(
        from_='+13343676244',
        body='It might rain bring an ☔',
        to='<your number>'
    )

else:
    print("good to go")
    message = client.messages.create(
        from_='+13343676244',
        body='It probably won\'t rain today',
        to='<your number>'
    )

print(message.status)
