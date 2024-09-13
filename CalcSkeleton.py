import tkinter as tk

calculation = "" # Variable stores the ongoing calculation as a string

# Function to add a symbol (number or operator) to the calculation
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol) # Append the symbol to the current calculation string
    text_result.delete(1.0, "end")  # Clear the text display
    text_result.insert(1.0, calculation)  # Insert the updated calculation into the display

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

# Function to clear the current calculation and reset the display
def clear_field():
    global calculation
    calculation = ""  # Reset the calculation string
    text_result.delete(1.0, "end")  # Clear the text display

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



# Create the main application window
root = tk.Tk()
root.geometry("300x275")  # Set the size of the window

# Text widget to display the calculation and result
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)  # Make the text display span across 5 columns

#Buttons
# Button No.1
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=4, column=1)
# Button No.2
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=4, column=2)
# Button No.3
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=4, column=3)
# Button No.4
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
# Button No.5
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
# Button No.6
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
# Button No.7
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=2, column=1)
# Button No.8
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=2, column=2)
# Button No.9
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=2, column=3)
# Button No.0
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=11, font=("Arial", 14))
btn_0.grid(row=5, column=1, columnspan=2)

# Plus Button
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=4, column=4)

# Minus Button
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)

# Multiply Button
btn_mul = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=2, column=4)

# Divide Button
btn_div = tk.Button(root, text="÷", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=1, column=4)

# Equals Button
btn_equals = tk.Button(root, text="=", command=evaluation_calculation, width=5, font=("Arial", 14))
btn_equals.grid(row=5, column=4)

# Decimal Button
btn_decimal = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_decimal.grid(row=5, column=3)

# Clear Button
btn_clear = tk.Button(root, text="AC", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=1, column=1)

# +/- Button (toggle between positive and negative numbers)
btn_plus_minus = tk.Button(root, text="+/-", command=toggle_sign, width=5, font=("Arial", 14))
btn_plus_minus.grid(row=1, column=2)

# Percentage Button (divide by 100 calculation)
btn_percentage = tk.Button(root, text="%", command=lambda: add_to_calculation("/100"), width=5, font=("Arial", 14))
btn_percentage.grid(row=1, column=3)

# Run the Tkinter event loop
root.mainloop()