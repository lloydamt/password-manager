from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
canvas_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_img)
canvas.grid(column=1, row=0)


"--------------------------------------------User Interface-------------------------------------------------------"
# Buttons
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37)
add_button.grid(column=1, row=4, columnspan=2, sticky=E)

# labels
website_label = Label(text="Website:", font=("Roboto", 10))
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=("Roboto", 10))
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Roboto", 10))
password_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "lloydamt@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)




window.mainloop()