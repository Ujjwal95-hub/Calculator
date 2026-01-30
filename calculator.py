# Calculator Program
import tkinter as tk
from tkinter import messagebox
import ast
import operator

def create_gui_calculator():
    # Create main window
    root = tk.Tk()
    root.title("Calculator")

    # Entry widget
    entry = tk.Entry(root, width=35, borderwidth=5)
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Allowed operators
    ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    # Safe evaluation function (math only)
    def safe_eval(expr):
        def _eval(node):
            if isinstance(node, ast.Constant):  # For numbers
                return node.value
            if isinstance(node, ast.BinOp):  # For operations like 2+3
                return ops[type(node.op)](_eval(node.left), _eval(node.right))
            raise ValueError("Invalid expression")

        parsed = ast.parse(expr, mode="eval")
        return _eval(parsed.body)

    def button_click(number):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + str(number))

    def button_clear():
        entry.delete(0, tk.END)
        
    def button_backspace():
        current = entry.get()
        if current:
            entry.delete(0, tk.END)
            entry.insert(0, current[:-1])

    def button_equal():
        try:
            result = safe_eval(entry.get())
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

    # Create buttons
    row = 1
    col = 0
    for button in buttons:
        if button == '=':
            tk.Button(root, text=button, padx=40, pady=20,
                      command=button_equal).grid(row=row, column=col)
        else:
            tk.Button(root, text=button, padx=40, pady=20,
                      command=lambda b=button: button_click(b)).grid(row=row, column=col)

        col += 1
        if col > 3:
            col = 0
            row += 1

    # Clear Button
    tk.Button(root, text="Clear", padx=85, pady=20,
              command=button_clear).grid(row=row, column = 0, columnspan=2)
    
    tk.Button(root, text="⌫", padx=85, pady=20,
              command=button_backspace).grid(row=row, column = 2, columnspan=2)

    # Keyboard shortcuts
    root.bind("<Return>", lambda e: button_equal())
    root.bind("<Escape>", lambda e: button_clear())
    root.bind("<BackSpace>", lambda e: button_backspace())

    root.mainloop()

# Run the GUI Calculator
create_gui_calculator()
