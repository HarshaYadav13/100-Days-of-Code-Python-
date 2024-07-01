from random import *
from tkinter import *
from tkinter import messagebox
# messagebox is not a class it's a module, so we have to import it separately as * only imports class
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }}

    if len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            # reading the existing data
            with open('password.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('password.json', 'w') as data_file:
                # writing data to the file
                json.dump(new_data, data_file, indent=4)
        else:
            # adding new data to the existing data
            data.update(new_data)

            with open('password.json', 'w') as data_file:
                # saving new data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)

        messagebox.showinfo(title="Saved", message="Password added successfully.")

    website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", padx=5, pady=5)
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.focus()  # to set the cursor in this text field
website_input.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:", padx=5, pady=5)
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.insert(END, string="@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", padx=5, pady=5)
password_label.grid(row=3, column=0)

password_input = Entry(width=22)
password_input.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, padx=3, pady=3, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
