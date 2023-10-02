from tkinter import *

win = Tk()
win.geometry("360x320")
win.resizable(0, 0)
win.title("Calculator")

def button_click(item):
    global expression
    if item == "=":
        try:
            result = str(eval(expression))
            input_text.set(result)
            expression = result
        except Exception as e:
            input_text.set("Error")
            expression = ""
    elif item == "C":
        expression = ""
        input_text.set("")
    elif item == "←":
        expression = expression[:-1]
        input_text.set(expression)
    else:
        expression += str(item)
        input_text.set(expression)

expression = ""
input_text = StringVar()

input_frame = Frame(win, width=400, height=100, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.grid(row=0, column=0, columnspan=4)
input_field = Entry(input_frame, font=('Arial', 24, 'bold'), textvariable=input_text, width=20, bg="#8E7A76", bd=0, justify=RIGHT)
input_field.pack(ipady=10, fill='both', expand=True)

btns_frame = Frame(win, width=400, height=400, bg="light blue")
btns_frame.grid(row=1, column=0, columnspan=4)

# Define button labels and their positions
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+', 'C', '←'  # Added 'C' and '←' buttons
]

# Create buttons using a loop
row_val = 1
col_val = 0
button_commands = {}

for button_label in button_labels:
    button = Button(btns_frame, text=button_label, fg="black", width=5, height=2, bd=0, bg="#eee", cursor="hand2",
                    command=lambda item=button_label: button_click(item))
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    button_commands[button_label] = button
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

win.mainloop()
