from tkinter import *
import ttkbootstrap
from tkinter import ttk

#Function to add a digit to display
def add_digit(digit):
    value = display.get()
    if value==0:
        value = digit
    else:
        value += digit
    
    display.delete(0, END)
    display.insert(0, value)

#Function to add an operaator to the display
def add_operator(operator):
    global first_num
    first_num = int(display.get())
    global math_operator
    math_operator = operator
    display.delete(0, END)

#Function to calculate the result
def calculate():
    second_num = int(display.get())
    display.delete(0, END)
    if math_operator == "+":
        result = first_num + second_num
    elif math_operator == "-":
        result = first_num - second_num
    elif math_operator == "*":
        result = first_num * second_num
    else:
        result = first_num / second_num
    
    display.insert(0, result)

#Function to clear the display
def clear():
    display.delete(0, END)
    display.insert(0, "0")

#Create the main window
root = ttkbootstrap.Window(themename="flatly")
root.title("Calculator")
root.geometry("280x400")
root.resizable(True,True)


#Create the display widget
display = ttk.Entry(root, font=("Helvetica", 27), justify=RIGHT)
display.insert(0,"0")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10)

#Create the digit buttons
button1 = ttk.Button(root, text="1", bootstyle = "dark", command=lambda: add_digit("1"))
button2 = ttk.Button(root, text="2", bootstyle = "dark", command=lambda: add_digit("2"))
button3 = ttk.Button(root, text="3", bootstyle = "dark", command=lambda: add_digit("3"))
button4 = ttk.Button(root, text="4", bootstyle = "dark", command=lambda: add_digit("4"))
button5 = ttk.Button(root, text="5", bootstyle = "dark", command=lambda: add_digit("5"))
button6 = ttk.Button(root, text="6", bootstyle = "dark", command=lambda: add_digit("6"))
button7 = ttk.Button(root, text="7", bootstyle = "dark", command=lambda: add_digit("7"))
button8 = ttk.Button(root, text="8", bootstyle = "dark", command=lambda: add_digit("8"))
button9 = ttk.Button(root, text="9", bootstyle = "dark", command=lambda: add_digit("9"))
button0 = ttk.Button(root, text="0", bootstyle = "dark", command=lambda: add_digit("0"))

#Create operator buttons
button_add = ttk.Button(root, text="+", bootstyle = "warning", command=lambda: add_operator("+"))
button_sub = ttk.Button(root, text="-", bootstyle = "warning", command=lambda: add_operator("-"))
button_mul = ttk.Button(root, text="*", bootstyle = "warning", command=lambda: add_operator("*"))
button_div = ttk.Button(root, text="/", bootstyle = "warning", command=lambda: add_operator("/"))

button_equal = ttk.Button(root, text="=", bootstyle = "success", command=calculate)
button_clear = ttk.Button(root, text="C", bootstyle = "danger", command=clear)

#Place the buttons on the grid
button1.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
button2.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
button3.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
button4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
button5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
button6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
button7.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
button8.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
button9.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
button0.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

button_add.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")
button_sub.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
button_mul.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
button_div.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
button_equal.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
button_clear.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

# ✅ Make grid cells expand with window
for i in range(5):  # total rows
    root.rowconfigure(i, weight=1)
for j in range(4):  # total columns
    root.columnconfigure(j, weight=1)


root.mainloop()