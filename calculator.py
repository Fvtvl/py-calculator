from tkinter import Tk, Entry, Button, StringVar


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""

        colors = {
            "bg": "#000000",
            "button": "#FFFFFF",
            "text": "#FFFFFF",
            "highlight": "#CCCCCC",
            "equal_button": "#2196F3",
            "clear_button": "#FFEB3B",
        }

        button_list = [
            ["(", 0, 50],
            [")", 90, 50],
            ["%", 180, 50],
            [7, 0, 125],
            [8, 90, 125],
            [9, 180, 125],
            [4, 0, 200],
            [5, 90, 200],
            [6, 180, 200],
            [1, 0, 275],
            [2, 90, 275],
            [3, 180, 275],
            [0, 90, 350],
            [".", 180, 350],
            ["+", 270, 275],
            ["-", 270, 200],
            ["/", 270, 50],
            ["*", 270, 125],
        ]

        def create_button(text, bg, command):
            return Button(
                width=11,
                height=4,
                text=text,
                relief="flat",
                fg=colors["bg"],
                bg=bg,
                command=command,
            )

        for btn_value, x, y in button_list:
            create_button(
                str(btn_value),
                colors["highlight"],
                lambda value=btn_value: self.show(value),
            ).place(x=x, y=y)

        create_button("=", colors["equal_button"], self.solve).place(x=270, y=350)
        create_button("C", colors["clear_button"], self.clear).place(x=0, y=350)

        Entry(
            width=17,
            fg=colors["text"],
            bg=colors["bg"],
            font=("Arial Bold", 28),
            textvariable=self.equation,
        ).place(x=0, y=0)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)


root = Tk()
calculator = Calculator(root)
root.mainloop()
