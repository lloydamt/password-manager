from tkinter import *
from tkinter import messagebox
import random
import pyperclip

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
canvas_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_img)
canvas.grid(column=1, row=0)


"---------------------------------Password Generator------------------------------------------------------------"
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)


"---------------------------------------Save to File---------------------------------------------------------------"
def add_entry():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="error", message="Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered\nEmail: {username}\n"
                                                              f"Password: {password} \nIs it ok to save?")
        if is_ok:
            with open("password_entries.txt", "a") as file:
                file.write(f"{website} | {username} | {password}")
                file.write("\n")
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
            website_entry.focus()


"--------------------------------------------User Interface-------------------------------------------------------"
# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37, command=add_entry)
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