# Calculator Program
import tkinter as tk
from tkinter import messagebox

def create_gui_calculator():
    # Create main window first
    root = tk.Tk()
    root.title("Calculator")
    
    # Entry widget - create it before the function that use it
    entry = tk.Entry(root, width = 35, borderwidth = 5)
    entry.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

    def button_click(number):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + str(number))
    
    def button_clear():
        entry.delete(0, tk.END)
        
    def button_equal():
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            messagebox.showerror("Error", "Invalid Calculation")

    # Define buttons
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    # Create Buttons
    row = 1
    col = 0
    for button in buttons:
        if button == '=' :
            tk.Button(root, text = button, padx = 40, pady = 20,
                      command = button_equal).grid(row = row, column = col)
        else:
            tk.Button(root, text = button, padx = 40, pady = 20,
                      command = lambda b = button: button_click (b)).grid(row = row, column = col)
        
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Clear Button
    tk.Button(root, text = "Clear", padx = 79, pady = 20,
              command = button_clear).grid(row = row, column = col, columnspan = 2)
    
    root.mainloop()

# Run the GUI Calculator
create_gui_calculator()
