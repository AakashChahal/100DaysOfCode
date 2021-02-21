import requests
from datetime import datetime
import smtplib

my_lat = <latitude here>
my_lng = <longitude here>
my_email = "<your email>"
my_pass = "<password>"
def iss_over():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lng = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    # print(iss_position)

    if my_lat - 5 <= iss_lat <= my_lat + 5 and my_lng - 5 <= iss_lng <= my_lng + 5:
        return True


def is_night():
    parameters = {
        "lat": my_lat,
        "lng": my_lng,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # print(sunrise)
    # print(sunset)
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


if is_night() and iss_over():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, my_pass)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject: Look up\n\nThe ISS is above you in the sky"
    )
