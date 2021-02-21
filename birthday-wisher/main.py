import pandas as pd
import random
import datetime as dt
import smtplib

data = pd.read_csv("birthdays.csv")
names = data["name"]
emails = data["email"]
dates = data["day"]
months = data["month"]
years = data["year"]

with open("quotes.txt") as file:
    quotes = file.readlines()
    quote = random.choice(quotes)

def send_wishes(to, message):
    connection = smtplib.SMTP("smtp.gmail.com")
    # connection.ehlo()
    connection.starttls()
    connection.login("<your email here>", "<your password here>")
    connection.sendmail("<your email here>", to, f"Subject: Happy Birthday!!\n\n{message}\nAnd here's quote for you as a gift:\n{quote}")
    connection.close()

def select_random_letter():
    letter_num = random.randint(1, 3)
    with open(f".\letter_templates\letter_{letter_num}.txt") as file:
        letter = file.read()

    return letter

def check_birthday():
    for name, email, date, month, year in zip(data["name"], data["email"], data["day"], data["month"], data["year"]):
        if dt.datetime.now().day == date and dt.datetime.now().month == month:
            birthday_letter = select_random_letter()
            birthday_letter = birthday_letter.replace("[NAME]", f"{name}").replace("[year]", f"{dt.datetime.now().year - year}")
            send_wishes(email, birthday_letter)


check_birthday()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
