import datetime
from tkinter import *
from tkinter import messagebox

import requests

today = datetime.datetime.now().date()
DATE = today.strftime("%Y%m%d")
USERNAME = "your username"
TOKEN = "your token"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "DSA graph",
#     "unit": "questions",
#     "type": "int",
#     "color": "sora"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


def call_put_pixel():
    put_pixel()


window = Tk()
window.title("Habit Tracker")
window.config(padx=30, pady=30)
window.config(bg="black")

header = Label(text="Habit Tracker", font=("Arial", 20, "bold"), padx=20, pady=20, bg="black", fg="blue")
header.grid(column=0, row=0, columnspan=2)
label1 = Label(text="How many questions?: ", padx=20, pady=20, bg="black", fg="white")
label1.grid(column=0, row=1)
num_questions = Entry()
num_questions.grid(column=1, row=1)
submit = Button(text="Submit", command=call_put_pixel, padx=5, pady=5)
submit.grid(column=0, row=2, columnspan=2)


def put_pixel():
    pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
    pixel_data = {
        "date": DATE,
        "quantity": f"{int(num_questions.get())}"
    }
    response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
    # print(response.text)
    num_questions.delete(0, END)
    messagebox.showinfo(title="Data Updated", message="Done!")


window.mainloop()
