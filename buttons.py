from tkinter import *
import numpy as np
from random import randint
from tkinter import messagebox
import sys

root = Tk()
root.title("Tic Tac Toe v2.0b")

buttons = []
for i in range(81):
    btn = Button(root, text="", font=("Arial 15 bold"), height=1, width=2,)
    btn.grid(row=int(i / 9), column=i % 9)
    buttons.append(btn)
    # if i % 3 == 0:
    #     buttons[i].grid(padx=0, 20)

# midlabel = Label(root, text="")
# midlabel.grid(row=0, column=3, padx=10)

restartButton = Button(root, text=("Restart"), font=("Arial 30 bold"), height=1, width=2, command=lambda: restart())
restartButton.grid(row=9, columnspan=9, sticky=S + N + E + W)

root.mainloop()
