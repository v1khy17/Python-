import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Initialize expression
        self.expression = ""
        self.result_var = tk.StringVar()

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root)
        display_frame.pack(expand=True, fill="both")

        # Display entry
        display_entry = tk.Entry(
            display_frame,
            textvariable=self.result_var,
            font=("Arial", 18),
            bd=30,
            insertwidth=4,
            width=14,
            borderwidth=4,
            justify="right",
        )
        display_entry.grid(row=0, column=0)

        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")

        # Button layout
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C"
        ]

        # Create and place buttons
        row = 0
        col = 0
        for button in buttons:
            if button == "=":
                cmd = self.evaluate
            elif button == "C":
                cmd = self.clear
            else:
                cmd = lambda x=button: self.add_to_expression(x)

            tk.Button(
                button_frame,
                text=button,
                font=("Arial", 18),
                borderwidth=1,
                relief="ridge",
                command=cmd,
            ).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Configure grid weights
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

    def add_to_expression(self, value):
        self.expression += str(value)
        self.result_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.result_var.set("")

    def evaluate(self):
        try:
            if self.expression:
                result = eval(self.expression)
                self.result_var.set(result)
                self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero!")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression!")
            self.clear()

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()