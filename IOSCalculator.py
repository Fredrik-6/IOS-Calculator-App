import tkinter as tk

calculation = "" # Variable stores the ongoing calculation as a string

# Function to add a symbol (number or operator) to the calculation
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol) # Append the symbol to the current calculation string
    text_result.delete(1.0, "end")  # Clear the text display
    text_result.insert(1.0, calculation)  # Insert the updated calculation into the display

# Function to handle operator press
def operator_action(operator, btn):
    global operator_pressed
    operator_pressed = operator

        # Highlight the pressed operator
    clear_operator_highlight()  # Clear previous highlights
    btn.config(bg="orange")  # Highlight the current button
    
    # Perform calculation if necessary (will update only when equals is pressed)
    if calculation:
        add_to_calculation(f" {operator} ")  # Separate operators from numbers

# Function to evaluate the calculation and display the result
def evaluation_calculation():
    global calculation
    try:
        calculation = str(eval(calculation)) # Evaluate the mathematical expression in the string
        text_result.delete(1.0, "end")  # Clear the display
        text_result.insert(1.0, calculation)  # Display the result
    except:
        clear_field()  # Clear the display if there is an error
        text_result.insert(1.0, "Error")  # Show an error message
    finally:
        operator_pressed = None
        clear_operator_highlight()  # Clear button highlight

# Function to clear the current calculation and reset the display
def clear_field():
    global calculation
    calculation = ""  # Reset the calculation string
    text_result.delete(1.0, "end")  # Clear the text display
    clear_operator_highlight()  # Clear operator highlight

# Function to toggle the sign of the current number
def toggle_sign():
    global calculation
    if calculation:  # Check if the calculation is not empty
        if calculation.startswith('-'):  # If the number is negative, remove the '-' sign
            calculation = calculation[1:]
        else:
            calculation = '-' + calculation  # If the number is positive, add a '-' sign
        text_result.delete(1.0, "end")  # Clear the text display
        text_result.insert(1.0, calculation)  # Insert the updated calculation

# Function to clear operator highlights
def clear_operator_highlight():
    for btn in operator_buttons:
        btn.config(bg="orange")  # Reset to original button color


# Create the main application window
root = tk.Tk()
root.geometry("320x475")  # Set the size of the window
root.title("iOS Calculator")

# Text widget to display the calculation and result
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), bg="#1c1c1c", fg="white")
text_result.grid(columnspan=4)

# Button styling for colors and layout like iOS
button_color = {
    "number": "#333333",  # Dark gray for numbers
    "operator": "#ff9500",  # Orange for operators
    "function": "#a5a5a5",  # Light gray for AC, +/- and %
    "zero": "#333333"  # Special button for zero
}

# Number buttons
number_buttons = [
    tk.Button(root, text=str(i), command=lambda i=i: add_to_calculation(i), width=5, height=2, font=("Arial", 18), bg=button_color["number"], fg="white") for i in range(10)
]

# Function buttons (AC, +/- and %)
btn_clear = tk.Button(root, text="AC", command=clear_field, width=5, height=2, font=("Arial", 18), bg=button_color["function"], fg="black")
btn_plus_minus = tk.Button(root, text="+/-", command=toggle_sign, width=5, height=2, font=("Arial", 18), bg=button_color["function"], fg="black")
btn_percentage = tk.Button(root, text="%", command=lambda: add_to_calculation("/100"), width=5, height=2, font=("Arial", 18), bg=button_color["function"], fg="black")

# Operator buttons (+, -, *, ÷) - highlight when clicked
operator_buttons = []
btn_div = tk.Button(root, text="÷", command=lambda: operator_action("/", btn_div), width=5, height=2, font=("Arial", 18), bg=button_color["operator"], fg="white")
btn_mul = tk.Button(root, text="×", command=lambda: operator_action("*", btn_mul), width=5, height=2, font=("Arial", 18), bg=button_color["operator"], fg="white")
btn_minus = tk.Button(root, text="-", command=lambda: operator_action("-", btn_minus), width=5, height=2, font=("Arial", 18), bg=button_color["operator"], fg="white")
btn_plus = tk.Button(root, text="+", command=lambda: operator_action("+", btn_plus), width=5, height=2, font=("Arial", 18), bg=button_color["operator"], fg="white")

operator_buttons.extend([btn_div, btn_mul, btn_minus, btn_plus])

# Equals button
btn_equals = tk.Button(root, text="=", command=evaluation_calculation, width=5, height=2, font=("Arial", 18), bg=button_color["operator"], fg="white")

# Decimal button
btn_decimal = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, height=2, font=("Arial", 18), bg=button_color["number"], fg="white")

# Layout - replicating the iOS calculator layout
btn_clear.grid(row=1, column=0)
btn_plus_minus.grid(row=1, column=1)
btn_percentage.grid(row=1, column=2)
btn_div.grid(row=1, column=3)

number_buttons[7].grid(row=2, column=0)
number_buttons[8].grid(row=2, column=1)
number_buttons[9].grid(row=2, column=2)
btn_mul.grid(row=2, column=3)

number_buttons[4].grid(row=3, column=0)
number_buttons[5].grid(row=3, column=1)
number_buttons[6].grid(row=3, column=2)
btn_minus.grid(row=3, column=3)

number_buttons[1].grid(row=4, column=0)
number_buttons[2].grid(row=4, column=1)
number_buttons[3].grid(row=4, column=2)
btn_plus.grid(row=4, column=3)

number_buttons[0].grid(row=5, column=0, columnspan=2)  # Zero button spans two columns
btn_decimal.grid(row=5, column=2)
btn_equals.grid(row=5, column=3)

# Run the application
root.mainloop()