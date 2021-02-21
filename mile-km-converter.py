import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# input for miles
input_miles = tkinter.Entry()
input_miles.grid(column=1, row=0)

# label miles
label1 = tkinter.Label(text="Miles", font=("Courier", 14, "italic"))
label1.grid(column=2, row=0)
label1.config(padx=20, pady=20)

label_eq = tkinter.Label(text="=", font=("Courier", 14, "bold"))
label_eq.grid(column=0, row=1)
label_eq.config(padx=20, pady=20)

# output in miles
output_km = tkinter.Label(text="0",  font=("Courier", 14))
output_km.grid(column=1, row=1)

# label miles
label2 = tkinter.Label(text="Km", font=("Courier", 14, "italic"))
label2.grid(column=2, row=1)
label2.config(padx=20, pady=20)


def conv():
    num_miles = float(input_miles.get())
    tot_km = num_miles * 1.609
    output_km.config(text=str(tot_km))


# calculate button
button = tkinter.Button(text="Convert", command=conv)
button.grid(column=1, row=2)

window.mainloop()
