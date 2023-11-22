import tkinter as tk
from tkinter import ttk
import subprocess

def login():
    global username_entry, password_entry
    username = entry_username.get()
    password = entry_password.get()

    # Check login credentials (placeholder logic)
    if username == "user" and password == "password":
        open_summary_page(username, password)
    else:
        print("Invalid login credentials")

def open_summary_page(username, password):
    # Execute the summary.py script with subprocess and pass username and password
    subprocess.run(["python", "summary.py", username, password])

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x200")
root.configure(bg="blue")  # Set background color to blue

# Create and place widgets
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=10)

entry_username = ttk.Entry(root)
entry_username.pack(pady=10)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)

entry_password = ttk.Entry(root, show="*")
entry_password.pack(pady=10)

login_button = ttk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
