import tkinter as tk
from tkinter import messagebox
import string
import random
import pyperclip  # To copy password to clipboard

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password should be at least 4 characters long.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    char_pool = ''
    if uppercase_var.get():
        char_pool += string.ascii_uppercase
    if lowercase_var.get():
        char_pool += string.ascii_lowercase
    if numbers_var.get():
        char_pool += string.digits
    if special_var.get():
        char_pool += string.punctuation

    if not char_pool:
        messagebox.showerror("Error", "Select at least one character type.")
        return

    password = ''.join(random.choice(char_pool) for _ in range(length))
    password_var.set(password)

# Copy password to clipboard
def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create GUI window
root = tk.Tk()
root.title("🔐 Advanced Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Title Label
tk.Label(root, text="Advanced Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Length Entry
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack()
length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify='center')
length_entry.pack(pady=5)

# Character type options
options_frame = tk.Frame(root)
options_frame.pack(pady=5)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Uppercase", variable=uppercase_var, font=("Arial", 10)).grid(row=0, column=0, sticky='w', padx=10)
tk.Checkbutton(options_frame, text="Lowercase", variable=lowercase_var, font=("Arial", 10)).grid(row=0, column=1, sticky='w', padx=10)
tk.Checkbutton(options_frame, text="Numbers", variable=numbers_var, font=("Arial", 10)).grid(row=1, column=0, sticky='w', padx=10)
tk.Checkbutton(options_frame, text="Special Characters", variable=special_var, font=("Arial", 10)).grid(row=1, column=1, sticky='w', padx=10)

# Generate button
tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

# Password display
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), justify='center', width=35, state='readonly')
password_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 10), bg="#2196F3", fg="white").pack(pady=5)

# Run the app
root.mainloop()
