from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
    pyperclip.copy(password)

# -------------------------------------- Search ------------------------------------------------------------------

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No data file found")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="error", message="Empty data file")
    else:
        if len(website) == 0:
            messagebox.showinfo(title="error", message="Please enter a website")
        elif website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="error", message="website does not exist in data")

        # isMatch = False
        # for (site, details) in data.items():
        #     if len(website) == 0:
        #         messagebox.showinfo(title="error", message="Please input a website")
        #         break
        #     if site == website:
        #         messagebox.showinfo(title=f"{site}", message=f'Email: {details["email"]} \n'
        #                                                         f'Password: {details["password"]}')
        #         isMatch = True
        # if not isMatch and len(website) > 0:
        #     messagebox.showinfo(title="error", message="Website does not exist in database")


"---------------------------------------Save to File---------------------------------------------------------------"
def add_entry():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="error", message="Please fill all fields")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered\nEmail: {username}\n"
        #                                                       f"Password: {password} \nIs it ok to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as read_file:
                data = json.load(read_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as file:
                data.update(new_data)
                json.dump(data, file, indent=4)

        finally:
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
                website_entry.focus()


"--------------------------------------------User Interface-------------------------------------------------------"
# Buttons
generate_button = Button(text="Generate Password", command=generate_password, width=15)
generate_button.grid(column=2, row=3, sticky=E)

add_button = Button(text="Add", width=45, command=add_entry)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

search_button = Button(text="Search", command=search, width=15)
search_button.grid(column=2, row=1, sticky=E)

# labels
website_label = Label(text="Website:", font=("Roboto", 10))
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=("Roboto", 10))
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Roboto", 10))
password_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
website_entry.focus()

username_entry = Entry(width=53)
username_entry.grid(column=1, row=2, columnspan=2, sticky=W)
username_entry.insert(0, "lloydamt@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, sticky=W)




window.mainloop()