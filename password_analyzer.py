import tkinter as tk
from tkinter import Toplevel, Button
import re
import hashlib

# Function to check password strength
def check_password():
    password = entry.get()

    # Checking for conditions
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/]', password))

    # Count conditions met
    conditions_met = sum([has_upper, has_lower, has_number, has_special])

    # Determine password strength
    suggestions = []
    
    if len(password) < 8:
        strength = "Weak"
        color = "#8B0000"  # Red
        suggestions.append("Your password is too short. Use at least 8 characters.")
    elif conditions_met == 4:
        strength = "Strong"
        color = "#28B463"  # Green
        suggestions.append("Good job! Your password is secure.")
    elif conditions_met == 3:
        strength = "Moderate"
        color = "#2980B9"  # Blue
        if not has_number:
            suggestions.append("Your password does not contain numbers.")
        if not has_special:
            suggestions.append("Your password does not contain special characters.")
        if not has_upper:
            suggestions.append("Your password does not contain uppercase letters.")
        if not has_lower:
            suggestions.append("Your password does not contain lowercase letters.")
    else:
        strength = "Weak"
        color = "#E74C3C"  # Red
        if has_upper and has_lower:
            suggestions.append("Your password does not contain numbers and special characters.")
        elif has_upper and has_number:
            suggestions.append("Your password does not contain lowercase letters and special characters.")
        elif has_lower and has_number:
            suggestions.append("Your password does not contain uppercase letters and special characters.")
        else:
            suggestions.append("Use a mix of uppercase, lowercase, numbers, and special characters.")

    # Create a new pop-up window
    popup = Toplevel(root)
    popup.title("Password Strength Result")
    popup.geometry("400x250")
    popup.configure(bg="#D6EAF8")  # Light blue background
    popup.grid_columnconfigure(0, weight=1)

    # Show password strength message with color
    tk.Label(
        popup, text=f"Strength: {strength}", font=("Arial", 12, "bold"), 
        fg=color, bg="#D6EAF8"
    ).grid(row=0, column=0, pady=10, sticky="n")

    # Show suggestions
    tk.Label(
        popup, text="Suggestion:", font=("Arial", 10, "bold"), 
        bg="#D6EAF8"
    ).grid(row=1, column=0, pady=5, sticky="n")

    # Center the suggestions
    for i, suggestion in enumerate(suggestions, start=2):
        tk.Label(
            popup, text=suggestion, wraplength=350, justify="center", 
            bg="#D6EAF8"
        ).grid(row=i, column=0, pady=3, sticky="n")

    # Hash button in pop-up
    Button(
        popup, text="Show Hash", command=lambda: show_hashed_password(password), 
        bg="#2980B9", fg="white", font=("Arial", 10, "bold"), bd=3, relief="ridge"
    ).grid(row=len(suggestions) + 2, column=0, pady=15)

# Function to toggle password visibility
def toggle_password():
    if show_password_var.get():
        entry.config(show="")  # Show password
    else:
        entry.config(show="*")  # Hide password

# Function to show hashed password in a new pop-up
def show_hashed_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Create a new pop-up for hash
    hash_popup = Toplevel(root)
    hash_popup.title("Password Hash")
    hash_popup.geometry("400x150")
    hash_popup.configure(bg="#F7DC6F")  # Light yellow background
    hash_popup.grid_columnconfigure(0, weight=1)

    tk.Label(
        hash_popup, text=f"SHA-256 Hash:\n{hashed_password}", padx=10, pady=10, 
        wraplength=350, justify="center", font=("Arial", 10, "bold"), bg="#F7DC6F"
    ).grid(row=0, column=0, pady=10)

# GUI setup
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x250")
root.configure(bg="#E5E7E9")  # Light gray background

# Label for password entry
tk.Label(root, text="Enter Password:", font=("Arial", 10, "bold"), bg="#E5E7E9").pack(pady=5)

# Password Entry
entry = tk.Entry(root, show="*", width=30, font=("Arial", 10))
entry.pack(pady=5)

# Show/Hide password checkbox 
show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(
    root, text="Show Password", variable=show_password_var, command=toggle_password, 
    bg="#E5E7E9", font=("Arial", 9)
)
show_password_checkbox.pack()

# Button to check strength
tk.Button(
    root, text="Check Strength", command=check_password, bg="#28B463", fg="white", 
    font=("Arial", 10, "bold"), bd=3, relief="ridge"
).pack(pady=15)

root.mainloop()
