# -----------------------------------------------#
# Description: A simple calculator using Tkinter #
# By Florian BAILLIEN                            #
# Date: 2024-10-07                               #
# Version: 1.0                                   #
# -----------------------------------------------#

# Import the Tkinter library
import tkinter as tk

# Import the math library
import math

# Fonction to add a number to the display
def button_click(value):
    current = display_var.get()
    # If the current value is 0, replace it with the new value
    if current == "0":
        display_var.set(value)
    else:
        display_var.set(current + value)

# Fonction to calculate the result
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception:
        display_var.set("Erreur")

# Fonction to clear the display
def clear_display():
    display_var.set("0")

# Fonction to change the sign of the number
def change_sign():
    current = display_var.get()
    if current != "0":
        if current[0] == "-":
            display_var.set(current[1:])
        else:
            display_var.set("-" + current)

# Fonction to calculate the square root
def square_root():
    try:
        result = math.sqrt(float(display_var.get()))
        display_var.set(str(result))
    except Exception:
        display_var.set("Erreur")

# Fonction to calculate the percentage
def percentage():
    try:
        result = float(display_var.get()) / 100
        display_var.set(str(result))
    except Exception:
        display_var.set("Erreur")

# Initialize the main window
root = tk.Tk()
root.title("Calculatrice")

# Block the window size
root.resizable(False, False)

# Variable for the display
display_var = tk.StringVar()
display_var.set("0")

# Crea
display = tk.Entry(root, textvariable=display_var, font=("Helvetica", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
display.grid(row=0, column=0, columnspan=4)

# Create button texts
button_texts = [
    ["C", "/", "*", "-"],
    ["7", "8", "9", "+"],
    ["4", "5", "6", "="],
    ["1", "2", "3", "√"],
    ["0", ".", "±", "%"]
]

# Create buttons
buttons = []
for i, row in enumerate(button_texts):
    for j, text in enumerate(row):
        if text == "":
            continue # Skip empty buttons
        elif text == "C":
            button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 18), command=clear_display)
        elif text == "=":
            button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 18), command=calculate)
        elif text == "±":
            button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 18), command=change_sign)
        elif text == "√":
            button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 18), command=square_root)
        elif text == "%":
            button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 18), command=percentage)
        else:
            button = tk.Button(root, text=text, padx=20, pady=20, font=("Helvetica", 18), command=lambda x=text: button_click(x))
        button.grid(row=i+1, column=j)
        buttons.append(button)

# Start the main event loop
root.mainloop()
