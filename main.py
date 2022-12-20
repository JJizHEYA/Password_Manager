from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import array


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# random password generator
def generate_password():
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']


    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)


    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x

    # print out password
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    # pyperclip helps us copy from the entry file like copy the random password for later use
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_list():
    # .get() get the variable from the address
    x = website_entry.get()
    y = email_entry.get()
    z = password_entry.get()
    # message box is used to show the messages as a pop-up box
    if x == "" or y == "" or z == "":
        messagebox.showerror(title="Data Entry Error", message="Plz fill up all the boxes")
    else:
        # message box ok or cancel if cancel then don't continue else continue
        is_okay = messagebox.askokcancel(title=x, message=f"the data entered \n website: {x} \n email:{y} \n password: {z} ")
        if is_okay:
            # creating a file and copying the entered data into the file
            with open(file="data.txt", mode="a") as file:
                file.write(f"{x} | {y} | {z} \n")

            # delete the values in the entry box after pressing add button
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# screen
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# logo
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels
website = Label(text="Website:", font=("arial", 10, "bold"))
website.grid(column=0, row=1, padx=5)

email = Label(text="Email/Username:", font=("arial", 10, "bold"))
email.grid(column=0, row=2, padx=5)

password = Label(text="Password:", font=("arial", 10, "bold"))
password.grid(column=0, row=3, padx=10)

# buttons
generate_pass = Button(text="Generate Password:", command=generate_password, highlightthickness=0)
generate_pass.grid(column=2, row=3, padx=10)

add_to_list = Button(text="Add", command=add_to_list, highlightthickness=0, width=44)
add_to_list.grid(column=1, row=4, columnspan=2, pady=10)

# Text input box
website_entry = Entry(window, width=52)
website_entry.grid(column=1, row=1, columnspan=2, pady=5)
website_entry.focus()

email_entry = Entry(window, width=52)
email_entry.grid(column=1, row=2, columnspan=2, pady=5)

password_entry = Entry(window, width=30)
password_entry.grid(column=1, row=3, pady=5)

window.mainloop()
