import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        #if the file is not present already,it will handle thos exception
        try:
            with open("data.json", "r") as data:
                # Reading old data from json
                old_data = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            # Updating the old data to new data
            old_data.update(new_data)


            with open("data.json", "w") as data:
                # Saving the new data into json text
                json.dump(old_data, data, indent=5)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)

# --------------------SEARCH-----------------------------------
def search():
    website=web_input.get()
    try:
        with open("data.json","r") as data:
            search_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in search_data:
            email=search_data[website]["email"]
            password = search_data[website]["password"]
            messagebox.showinfo(title=web_input.get(),message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)
# label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pa_label = Label(text="")
pa_label.grid(column=0, row=4)
# input
web_input = Entry(width=40)
web_input.grid(column=1, row=1)
web_input.focus()
email_input = Entry(width=40)
email_input.grid(column=1, row=2)
email_input.insert(0, "example@gmail.com")

pass_input = Entry(width=40)
pass_input.grid(column=1, row=3)

# button
search_button = Button(text="Search",width=15,command=search)
search_button.grid(column=3,row=1)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=3, row=3)

add_button = Button(text="Add", width=16, command=save)
add_button.grid(column=0, row=4, columnspan=2)
# messagebox.showinfo(title="Description",message="This Tkinter-based Python password manager simplifies secure password management. Add a password with website details, generate strong passwords, and search stored credentials. Error messages provide guidance, and your data is stored in 'data.json' for convenience. Streamline your password management with this user-friendly tool.")

window.mainloop()
