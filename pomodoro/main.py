from tkinter import *
import time
import math
import winsound
# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f9f9dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

check = "🏁"
checks = ""
reps = 0
# TIMER RESET
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")


# TIMER MECHANISM
def start_timer():
    global reps, checks
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        checks += check
        check_labels.config(text=checks)
        title_label.config(text="Break", font=(FONT_NAME, 40), bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        checks += check
        check_labels.config(text=checks)
        title_label.config(text="Break", font=(FONT_NAME, 40), bg=YELLOW, fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Work", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)



# COUNTDOWN MECHANISM
def countdown(count):
    global timer
    min_count = math.floor(count / 60)
    if min_count < 10:
        min_count = "0"+str(min_count)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = "0"+str(sec_count)
    if count > 0:
        timer = window.after(1000, countdown, count-1)
        canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    else:
        winsound.Beep(900, 2000)
        start_timer()


# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_labels = Label(font=(FONT_NAME, 14, "bold"), bg=YELLOW, fg=GREEN)
check_labels.grid(column=1, row=3)

window.mainloop()
