from tkinter import *
import os
from tkinter import messagebox
import random
BG_COLOR = "#ffffff"

# Generate password
def generate_pass():
    small = [chr(x) for x in range(65, 91)]
    caps = [chr(x) for x in range(97, 123)]
    nums = list(map(str, [x for x in range(10)]))
    symbols = ['~','!','@','#','$','%','^','&','*','(',')','_','+','=','-','?','/','>','.','<']

    length = random.randint(8, 16)
    combination = small + caps + nums + symbols
    random.shuffle(combination)
    user_pass = ''.join(random.sample(combination, length))
    password.insert(0, user_pass)

# save password
def save_pass():
    website = web_name.get()
    user_email = email.get()
    user_pass = password.get()
    if website == "" or user_email == "" or user_pass == "":
        messagebox.showerror(title="Error", message="You didn't enter any value")
    else:
        save = messagebox.askyesno(title="Save Detalis?", message="Do you want to save the entered details?")
        if save:
            if os.path.exists(".\my_passwords.txt"):
                with open("my_passwords.txt", "a") as file:
                    file.write(f"{str(website)} | {str(user_email)} | {str(user_pass)}\n")
                messagebox.showinfo(title="Message", message="Password saved")

            else:
                with open("my_passwords.txt", "w") as file:
                    file.write(f"{str(website)} | {str(user_email)} | {str(user_pass)}\n")

            web_name.delete(0, END)
            password.delete(0, END)

# UI
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(width=230, height=230, bg=BG_COLOR, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website name
label1 = Label(text="Website: ", bg=BG_COLOR, padx=5, pady=5)
label1.grid(column=0, row=1)
web_name = Entry(width=51)
web_name.focus()
web_name.grid(column=1, row=1, columnspan=2)

# email
label2 = Label(text="Email: ", bg=BG_COLOR, padx=5, pady=5)
label2.grid(column=0, row=2)
email = Entry(width=51)
email.insert(0, "mostusedemail@gmail.com")
email.grid(column=1, row=2, columnspan=2)

# Password
label3 =  Label(text="Password: ", bg=BG_COLOR, padx=5, pady=5)
label3.grid(column=0, row=3)
password = Entry(width=30)
password.grid(column=1, row=3)
gen_pass = Button(text="Generate Password", command=generate_pass)
gen_pass.grid(column=2, row=3)

# save Button
save_button = Button(text="Add", width=40, padx=5, pady=5, command=save_pass)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
