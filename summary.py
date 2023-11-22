import tkinter as tk
from tkinter import ttk
from data_storage import create_table, save_user_data
import sys
import subprocess

# Retrieve username and password from command line arguments
username = sys.argv[1] if len(sys.argv) > 1 else "user"  # Default to "user" if not provided
password = sys.argv[2] if len(sys.argv) > 2 else "password"  # Default to "password" if not provided

def calculate_total():
    apples_price = float(entry_apples.get())
    book_price = float(entry_book.get())
    car_price = float(entry_car.get())

    total_cost = apples_price + book_price + car_price
    label_total.config(text=f'Total Cost: ${total_cost:.2f}')

    # Save user data to the database
    save_user_data(username, password, apples_price, book_price, car_price)

def go_back():
    summary_page.destroy()  # Close the current summary page
    subprocess.run(["python", "main.py"])  # Run main.py

# Initialize the database table
create_table()

# Create summary page
summary_page = tk.Tk()
summary_page.title("Summary Page")
summary_page.geometry("400x200")

# Create and place widgets
label_apples = tk.Label(summary_page, text="Apples:")
label_apples.grid(row=0, column=0, padx=10, pady=10)

entry_apples = ttk.Entry(summary_page)
entry_apples.grid(row=0, column=1, padx=10, pady=10)

label_book = tk.Label(summary_page, text="Book:")
label_book.grid(row=1, column=0, padx=10, pady=10)

entry_book = ttk.Entry(summary_page)
entry_book.grid(row=1, column=1, padx=10, pady=10)

label_car = tk.Label(summary_page, text="Car:")
label_car.grid(row=2, column=0, padx=10, pady=10)

entry_car = ttk.Entry(summary_page)
entry_car.grid(row=2, column=1, padx=10, pady=10)

calculate_button = ttk.Button(summary_page, text="Calculate Total", command=calculate_total)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

label_total = tk.Label(summary_page, text="Total Cost: $0.00")
label_total.grid(row=4, column=0, columnspan=2, pady=10)

back_button = ttk.Button(summary_page, text="Go Back", command=go_back)
back_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop for the summary page
summary_page.mainloop()
