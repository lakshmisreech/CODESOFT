import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("570x600+500+100")
root.resizable(False, False)
root.configure(bg="white")

equation = ""

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

def backspace():
    global equation
    equation = equation[:-1]
    label_result.config(text=equation)

label_result = tk.Label(root, width=25, height=2, text="", font=("arial", 30), bd=1, fg="white", bg="#fe9037")
label_result.pack()

def create_oval_button(text, x, y, command, width=120, height=70):
    canvas = tk.Canvas(root, width=width, height=height, bg="white", highlightthickness=0)
    canvas.place(x=x, y=y)
    canvas.create_oval(5, 5, width - 5, height - 5, fill="#fe9037", outline="white", width=2)
    canvas.create_text(width // 2, height // 2, text=text, fill="white", font=("arial", 30, "bold"))
    canvas.bind("<Button-1>", lambda e: command())

button_params = [
    ("C", 10, 100, clear), ("/", 150, 100, lambda: show("/")), ("%", 290, 100, lambda: show("%")), ("*", 430, 200, lambda: show("*")),
    ("7", 10, 200, lambda: show("7")), ("8", 150, 200, lambda: show("8")), ("9", 290, 200, lambda: show("9")), ("-", 430, 300, lambda: show("-")),
    ("4", 10, 300, lambda: show("4")), ("5", 150, 300, lambda: show("5")), ("6", 290, 300, lambda: show("6")), ("+", 430, 400, lambda: show("+"), 120, 70),
    ("1", 10, 400, lambda: show("1")), ("2", 150, 400, lambda: show("2")), ("3", 290, 400, lambda: show("3")),
    ("0", 10, 500, lambda: show("0"), 250, 70), (".", 290, 500, lambda: show("."), 120, 70), ("=", 430, 500, calculate, 120, 70), ("<", 430, 100, backspace, 120, 70)
]

for params in button_params:
    if len(params) == 6:
        text, x, y, command, width, height = params
        create_oval_button(text, x, y, command, width, height)
    else:
        text, x, y, command = params
        create_oval_button(text, x, y, command)

root.mainloop()
