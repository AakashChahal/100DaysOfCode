BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
try:
    FILE = pd.read_csv(".\data\words_to_learn.csv")
except:
    FILE = pd.read_csv(".\\data\\french_words.csv")
CARDS = FILE.to_dict(orient="records")
curr_card = {}

# flip card
def flip_card():
    canvas.itemconfig(flash_card, image=back_flash_card)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=curr_card["English"], fill="white")

# remove learnt words from learnt list
def word_learnt():
    CARDS.remove(curr_card)
    data = pd.DataFrame(CARDS)
    data.to_csv(".\data\words_to_learn.csv", index=False)
    next_word()

# display new random words
def next_word():
    global curr_card, card
    window.after_cancel(card)
    curr_card = random.choice(CARDS)
    canvas.itemconfig(flash_card, image=front_flash_card)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=curr_card["French"], fill="black")
    window.after(3000, flip_card)

# UI for the app
window = Tk()
window.title("Capstone Project")
window.config(width=1000, height=1000, bg=BACKGROUND_COLOR, padx=20, pady=20)

canvas = Canvas(width=1000, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
front_flash_card = PhotoImage(file=".\images\card_front.png")
back_flash_card = PhotoImage(file=".\images\card_back.png")
flash_card = canvas.create_image(500, 280, image=front_flash_card)
title = canvas.create_text(500, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(500, 250, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

card = window.after(3000, flip_card)

wrong_img = PhotoImage(file=".\images\wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong.grid(column=0, row=1)

right_img = PhotoImage(file=".\images\\right.png")
right = Button(image=right_img, highlightthickness=0, command=word_learnt)
right.grid(column=1, row=1)

next_word()

window.mainloop()
