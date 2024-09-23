from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    # The code above can we shortened down to one line as followed:
    password = "".join(password_list)
    password_text.insert(0, password)
    # print(f"Your password is: {password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="please Do not leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                              f"Website: {website}\n"
                                                              f"Email: {email}\n"
                                                              f"Password: {password}\n"
                                                              f"Do you wish to proceed?")

        # This function is invoked when button `submit` is clicked
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_text.delete(0, END)
                password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="website")
website_label.grid(column=0, row=1)
email_label = Label(text="E-mail/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_text = Entry(width=35)
website_text.grid(column=1, row=1, columnspan=2)
website_text.focus()
email_text = Entry(width=35)
email_text.grid(column=1, row=2, columnspan=2)
email_text.insert(0, "hamza.dahir@hotmail.com")
password_text = Entry(width=21)
password_text.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
