# Import necessary modules
import sqlite3
from tkinter import *
from tkinter import messagebox

# Create the address book application window
root = Tk()
root.title("Address Book")
root.geometry("500x400")

# Create a function to connect to the database
def connect():
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT
        )
    """)
    conn.commit()
    conn.close()

# Create a function to display a message box
def show_message_box(title, message):
    messagebox.showinfo(title, message)

# Create a function to add a new contact
def add_contact():
    # Get input from the user
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    # Connect to the database
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()

    # Insert the new contact into the database
    cursor.execute("""
        INSERT INTO contacts (first_name, last_name, email, phone)
        VALUES (?, ?, ?, ?)
    """, (first_name, last_name, email, phone))

    conn.commit()
    conn.close()

    # Show a success message
    show_message_box("Success", "Contact added successfully")

    # Clear the input fields
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)

# Create labels and entry fields for input
first_name_label = Label(root, text="First Name:")
first_name_label.pack()
first_name_entry = Entry(root)
first_name_entry.pack()

last_name_label = Label(root, text="Last Name:")
last_name_label.pack()
last_name_entry = Entry(root)
last_name_entry.pack()

email_label = Label(root, text="Email:")
email_label.pack()
email_entry = Entry(root)
email_entry.pack()

phone_label = Label(root, text="Phone:")
phone_label.pack()
phone_entry = Entry(root)
phone_entry.pack()

# Create a button to add a new contact
add_button = Button(root, text="Add Contact", command=add_contact)
add_button.pack()

# Call the connect function to setup the database
connect()

# Run the main loop
root.mainloop()