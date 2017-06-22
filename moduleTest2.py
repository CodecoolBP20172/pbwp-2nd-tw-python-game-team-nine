from tkinter import *
import numpy as np
from random import randint
from tkinter import messagebox
import sys

root = Tk()
root.title("Tic Tac Toe v2.0b")


calctab = np.array([[0] * 9] * 9)
calctabsmall = np.array([[0] * 3] * 3)
playfield = np.array([[" "] * 9] * 9)
playfieldsmall = np.array([[" "] * 3] * 3)

buttons = []
for i in range(81):
    btn = Button(root, text="", font=("Arial 15 bold"), height=1, width=2, command=lambda i=i: ttt(i))
    btn.grid(row=int(i / 9), column=i % 9, sticky=S + N + E + W)
    buttons.append(btn)

# midlabel = Label(root, text="")
# midlabel.grid(row=0, column=3, padx=10)

restartButton = Button(root, text=("Restart"), font=("Arial 30 bold"), height=1, width=2, command=lambda: restart())
restartButton.grid(row=9, columnspan=9, sticky=S + N + E + W)

bclick = True


def deactivate_buttons(n):
    for i in range(81):
        buttons[i].configure(state=DISABLED)
    i, j = n // 9, n % 9
    si, sj = i % 3, j % 3
    # (si vagy sj * 3)+ 0, 1, 2
    for c in range(9):
        bi = (si * 3 + c // 3) * 9 + (sj * 3 + c % 3)
        buttons[bi].configure(state=NORMAL)


def ttt(n):

    print(n)
    global bclick
    if buttons[n]["text"] == "" and bclick:  # player 1 click
        buttons[n]["text"] = "X"
        bclick = False
        calctab[n // 9, n % 9] = 1
    elif buttons[n]["text"] == "" and bclick is False:  # player 2 click
        buttons[n]["text"] = "O"
        bclick = True
        calctab[n // 9, n % 9] = -1
    bigwincheck()
    print(calctab)
    print(calctabsmall)
    for i in range(9):
        if calctabsmall[i // 3, i % 3] == 1:

            btn2 = Button(root, text="X", state=DISABLED, font=("Arial 45 bold"), height=1, width=1)
            btn2.grid(row=i // 3 * 3, column=i % 3 * 3, rowspan=3, columnspan=3, sticky=S + N + W + E)
        if calctabsmall[i // 3, i % 3] == -1:
            btn2 = Button(root, text="O", font=("Arial 15 bold"), height=3, width=2)
            btn2.grid(row=i // 3 * 3, column=i % 3 * 3, rowspan=3, columnspan=3, sticky=S + N + W + E)
    deactivate_buttons(n)


def restart():
    # if wincheck() == "o" or wincheck() == "x" or wincheck() == "tie":
    #     for i in range(3):
    #         for j in range(3):
    #             calctab[i, j] = 0
    #             playfield[i, j] = " "
    for i in range(81):
        buttons[i]["text"] = ""


def bigwincheck():

    k, i = None, None
    x, y = k, i
    for n in range(81):
        if n % 3 == 0:
            wincounth, wincountv, wincountd, wincountd2 = 0, 0, 0, 0
        k = n // 9
        i = n // 3 - ((n // 9) * 3) + ((n // 27) * 3)
        j = n - (n // 3 - ((n // 9) * 3) + ((n // 27) * 3)) * 3 - (n // 9) * 6
        wincounth = wincounth + calctab[i, j]
        wincountv = wincountv + calctab[j, i]
        if k != x or i % 3 == 0:
            x, y = k, i
            wincountd = wincountd + calctab[i + n % 3, j]
            wincountd2 = wincountd2 + calctab[i + n % 3, n // 9 * 3 + abs(j % 3 - 2) - n // 27 * 9]

        if abs(wincounth) == 3 or abs(wincountd) == 3 or abs(wincountd2) == 3:
            calctabsmall[k // 3, k % 3] = int(wincounth / 3) + int(wincountd / 3) + int(wincountd2 / 3)

        if abs(wincountv) == 3:
            calctabsmall[k % 3, k // 3] = int(wincountv / 3)


def smallwincheck():
    playerwins = False
    if playerwins is False:
        wincountd, wincountd2 = 0, 0
        for i in range(9):
            if i % 3 == 0:
                wincounth, wincountv = 0, 0
            wincounth = wincounth + calctabsmall[i // 3, i % 3]
            wincountv = wincountv + calctabsmall[i % 3, i // 3]
            if i % 3 == 0:
                wincountd = wincountd + calctabsmall[i // 3, i // 3]
                wincountd2 = wincountd2 + calctabsmall[i // 3, 2 - i // 3]
            if abs(wincounth) == 3 or abs(wincountv) == 3 or abs(wincountd) == 3 or abs(wincountd2) == 3:
                playerwins = True
                break

        n = 0
        for i in range(3):
            for j in range(3):
                if calctab[i, j] == 0:
                    n = n + 1
        if n == 0:
            return "tie"

    if wincounth == 3 or wincountv == 3 or wincountd == 3 or wincountd2 == 3:
        return "x"
    elif wincounth == -3 or wincountv == -3 or wincountd == -3 or wincountd2 == -3:
        return "y"
    else:
        return "senki"


root.mainloop()
