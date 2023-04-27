from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False,False)

        self.equation=StringVar()
        self.entry_value=''

        button_list = [
            ['(', 0, 50], [')', 90, 50], ['%', 180, 50],
            [1, 0, 125], [2, 90, 125], [3, 180, 125],
            [4, 0, 200], [5, 90, 200], [6, 180, 200],
            [7, 0, 275], [8, 180, 275], [9, 90, 275],
            [0, 90, 350], ['.', 180, 350],
            ['+', 270, 275], ['-', 270, 200], ['/', 270, 50], ['*', 270, 125]
        ]

        for btn_value, x, y in button_list:
            Button(width=11, height=4, text=str(btn_value), relief='flat', bg='white', command=lambda value=btn_value: self.show(value)).place(x=x ,y=y)

        Button(width=11, height=4, text="=", relief='flat', bg='lightblue', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text="C", relief='flat', command=self.clear).place(x=0 ,y=350)
        
        Entry(width=17, bg='#ccddff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0,y=0)

    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)

    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)

root=Tk()
calculator=Calculator(root)
root.mainloop()