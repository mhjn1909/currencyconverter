import tkinter as tk
from tkinter import ttk

# Hardcoded exchange rates for simplicity
# Replace these with dynamic API calls for real-time conversion
exchange_rates = {
    "USD": 1.0,        # Base currency
    "EUR": 0.92,       # Example rate
    "GBP": 0.8,        # Example rate
    "INR": 82.5,       # Example rate
    "JPY": 145.0,      # Example rate
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()

        # Conversion logic
        converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# Title label
title_label = tk.Label(root, text="Currency Converter", font=("Arial", 16))
title_label.pack(pady=10)

# Amount entry
amount_label = tk.Label(root, text="Amount:")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# From currency selection
from_currency_label = tk.Label(root, text="From:")
from_currency_label.pack(pady=5)
from_currency_combo = ttk.Combobox(root, values=list(exchange_rates.keys()))
from_currency_combo.pack(pady=5)
from_currency_combo.set("USD")  # Default selection

# To currency selection
to_currency_label = tk.Label(root, text="To:")
to_currency_label.pack(pady=5)
to_currency_combo = ttk.Combobox(root, values=list(exchange_rates.keys()))
to_currency_combo.pack(pady=5)
to_currency_combo.set("EUR")  # Default selection

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Run the application
root.mainloop()
