import tkinter as tk
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="contact_manager"
)

cursor = db.cursor()

def add_contact():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()

    # Insert the contact into the database
    cursor.execute("INSERT INTO contacts (first_name, last_name, email) VALUES (%s, %s, %s)", (first_name, last_name, email))
    db.commit()
    clear_entries()
    display_contacts()

def display_contacts():
    contact_listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact[1]} {contact[2]} - {contact[3]}")

def clear_entries():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Manager")

# Create and place labels, entry fields, and buttons
first_name_label = tk.Label(root, text="First Name")
first_name_label.pack()
first_name_entry = tk.Entry(root)
first_name_entry.pack()

last_name_label = tk.Label(root, text="Last Name")
last_name_label.pack()
last_name_entry = tk.Entry(root)
last_name_entry.pack()

email_label = tk.Label(root, text="Email")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

contact_listbox = tk.Listbox(root)
contact_listbox.pack()

display_contacts()

root.mainloop()

# Close the database connection when the application exits
db.close()
