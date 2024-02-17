from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = '#FFFFFF'
DARKBLUE = '#00008B'
file_text = ''

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global file_text

    with open("user_data.txt", "w") as user_data:

        file_text += website_input.get() + ' | ' + email_input.get() + ' | ' + password_input.get() + '\n'
        user_data.write(file_text)

    website_input.delete(0,'end') #Deletes from 0th character to the 'end' character
    #email_input.delete(0, 'end')] #Assumes that you want to use the same email...
    password_input.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg=DARKBLUE ,padx= 50, pady= 50)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg=DARKBLUE, highlightthickness=0)  # Highlight thickness gets rid of border
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)  # If using grid can ONLY use grid

# LABELS
website_label = Label(text='Website', fg=WHITE, bg=DARKBLUE)
website_label.grid(row=1, column=0)
website_label.focus()

email_label = Label(text='Email/Username', fg=WHITE, bg=DARKBLUE)
email_label.grid(row=2, column=0)

password_label = Label(text='Password', fg=WHITE, bg=DARKBLUE)
password_label.grid(row=3, column=0)

# INPUTS
website_input = Entry(width=50)
website_input.insert(END, string="Enter your website:")
website_input.grid(column=1, row=1, columnspan=2)

email_input = Entry(width=50)
email_input.insert(END, string="stephen@email")
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=31, highlightthickness=0)
password_input.insert(END, string="Enter your password:")
password_input.grid(column=1, row=3)

# BUTTONS
generatepassword_button = Button(text='Generate Password', width=14)
generatepassword_button.grid(column=2, row=3)

add_button = Button(text='Add', width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()  # Ends the program.
