Creating a calculator in Python can be done either in a console-based format or using a GUI (Graphical User Interface). Below are examples of both:

Console-Based Calculator in Python
This simple Python program can perform basic arithmetic operations like addition, subtraction, multiplication, or division depending on the user input.

python

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

# Main program
def main():
    print("Select operation -\n" \
          "1. Add\n" \
          "2. Subtract\n" \
          "3. Multiply\n" \
          "4. Divide\n")

    # Taking input from the user
    choice = int(input("Select operations from 1, 2, 3, 4:"))
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if choice == 1:
        print(f"{number1} + {number2} = {add(number1, number2)}")
    elif choice == 2:
        print(f"{number1} - {number2} = {subtract(number1, number2)}")
    elif choice == 3:
        print(f"{number1} * {number2} = {multiply(number1, number2)}")
    elif choice == 4:
        print(f"{number1} / {number2} = {divide(number1, number2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
GUI-Based Calculator Using Tkinter
This program uses the Tkinter library to create a simple GUI for a calculator.

python

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to show calculations
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to add a digit or operator to the entry widget
def button_click(item):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(item))

# Function to clear the entry widget
def button_clear():
    entry.delete(0, tk.END)

# Function for arithmetic operations
def button_operation(operator):
    first_number = entry.get()
    global f_num
    global operation
    operation = operator
    f_num = float(first_number)
    entry.delete(0, tk.END)

# Function for the equal button
def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if operation == "+":
        entry.insert(0, f_num + float(second_number))
    elif operation == "-":
        entry.insert(0, f_num - float(second_number))
    elif operation == "*":
        entry.insert(0, f_num * float(second_number))
    elif operation == "/":
        entry.insert(0, f_num / float(second_number))

# Define calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0)
]

# Create digit buttons
for (text, row, col) in buttons:
    tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Create operation buttons
tk.Button(root, text='+', padx=39, pady=20, command=lambda: button_operation("+")).grid(row=1, column=3)
tk.Button(root, text='-', padx=41, pady=20, command=lambda: button_operation("-")).grid(row=2, column=3)
tk.Button(root, text='*', padx=40, pady=20, command=lambda: button_operation("*")).grid(row=3, column=3)
tk.Button(root, text='/', padx=41, pady=20, command=lambda: button_operation("/")).grid(row=4, column=3)

# Create other buttons
tk.Button(root, text='Clear', padx=79, pady=20, command=button_clear).grid(row=4, column=1, columnspan=2)
tk.Button(root, text='=', padx=91, pady=20, command=button_equal).grid(row=5, column=0, columnspan=4)

# Main loop
root.mainloop()
This code creates a functioning calculator GUI. Save the code in a .py file and run it using a Python interpreter to see the calculator on your screen.

How To Make a Calculator Program in Python 3
digitalocean.com

Python Program to Make a Simple Calculator
geeksforgeeks.org

How to Make a Calculator With Python {in 5 Steps}
phoenixnap.com
