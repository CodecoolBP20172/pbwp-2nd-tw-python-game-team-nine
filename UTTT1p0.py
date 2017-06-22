from tkinter import *
import numpy as np
from tkinter import messagebox
import sys

root = Tk()
root.title("Ultimate Tic Tac Toe")

calctab = np.array([[0] * 9] * 9)
calctabsmall = np.array([[0] * 3] * 3)

bigbuttons = []
for j in range(9):
    btn2 = Button(root, text="", state=DISABLED, font=("Arial 45 bold"), height=1, width=1)
    btn2.grid(row=j // 3 * 3, column=j % 3 * 3, rowspan=3, columnspan=3, sticky=S + N + W + E)
    bigbuttons.append(btn2)

buttons = []
for i in range(81):
    btn = Button(root, text="", font=("Arial 15 bold"), height=1, width=2,
                 bg="pale green", command=lambda i=i: playermove(i))
    btn.grid(row=int(i / 9), column=i % 9, sticky=S + N + E + W)
    buttons.append(btn)
    if i % 3 == 0:
        buttons[i].grid(padx=(10, 0))
    if i % 3 == 2:
        buttons[i].grid(padx=(0, 10))
    if (i // 9) % 3 == 0:
        buttons[i].grid(pady=(10, 0))
    if (i // 9) % 3 == 2:
        buttons[i].grid(pady=(0, 10))


restartButton = Button(root, text=("Restart"), font=("Arial 30 bold"),
                       state=DISABLED, height=1, width=2, command=lambda: restart())
restartButton.grid(row=9, columnspan=9, sticky=S + N + E + W)

messagebox.showinfo("Game Rules", "Like the original Tic-Tac-Toe, Player 1"
                    "is represented by X and Player 2 is represented by O."
                    "To start the game, Player 1 places an X on any one of the 81 empty squares, "
                    "and then players alternate turns. However, after the initial move, "
                    "players must play the board that mirrors the square from the previous player."
                    "If the next move is to a board that has already been won, then that player may choose "
                    "an open square on any board for that turn. You win boards as usual, but you win the game "
                    "when you win three boards together (across rows, columns or diagnols).")

bclick = True


def deactivate_buttons(n):
    for i in range(81):
        buttons[i].configure(state=DISABLED, background="misty rose")
    i, j = n // 9, n % 9
    si, sj = i % 3, j % 3
    if abs(calctabsmall[si, sj]) == 1 or calctabsmall[si, sj] == 6:
        for i in range(81):
            buttons[i].configure(state=NORMAL, background="pale green")

    for c in range(9):
        bi = (si * 3 + c // 3) * 9 + (sj * 3 + c % 3)
        buttons[bi].configure(state=NORMAL, background="pale green")


def playermove(n):
    if smallwincheck() != "y" and smallwincheck() != "x" and smallwincheck() != "tie":
        global bclick
        c = 0
        for i in range(9):
            for j in range(9):
                c = c + calctab[i, j]
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
                bigbuttons[i].tkraise()
                bigbuttons[i]["text"] = "X"
            elif calctabsmall[i // 3, i % 3] == -1:
                bigbuttons[i].tkraise()
                bigbuttons[i]["text"] = "O"
            elif calctabsmall[i // 3, i % 3] == 6:
                bigbuttons[i].tkraise()
                bigbuttons[i]["text"] = "T"
        d = 0
        for i in range(9):
            for j in range(9):
                d = d + calctab[i, j]
        if c != d:
            deactivate_buttons(n)
        if smallwincheck() == "x":
            print("Player one wins!")
            messagebox.showinfo("Result", "Player One wins!")

        elif smallwincheck() == "y":
            print("Player two wins!")
            messagebox.showinfo("Result", "Player Two wins!")

        elif smallwincheck() == "tie":
            print("Tie")
            messagebox.showinfo("Result", "Tie!")
        if smallwincheck() == "x" or smallwincheck() == "y" or smallwincheck() == "tie":
            restartButton.configure(state=NORMAL)


def restart():
    if smallwincheck() == "y" or smallwincheck() == "x" or smallwincheck() == "tie":
        for n in range(81):
            k = n // 9
            i = n // 3 - ((n // 9) * 3) + ((n // 27) * 3)
            j = n - (n // 3 - ((n // 9) * 3) + ((n // 27) * 3)) * 3 - (n // 9) * 6
            calctab[i, j] = 0
            calctabsmall[i // 3, i % 3] = 0
            buttons[n].tkraise()
            buttons[n].configure(text="", state=NORMAL, background="pale green")
        restartButton.configure(state=DISABLED)
    print(calctab)
    print(calctabsmall)


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

        if n % 9 == 0:
            tie = 0
        if calctab[i, j] == 0:
            tie = tie + 1
        if n % 9 == 8 and tie == 0 and calctabsmall[k // 3, k % 3] == 0:
            calctabsmall[k // 3, k % 3] = 6


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

    n, m = 0, 0
    for i in range(9):  # check if the two diagonals are tied or not
        if i % 3 == 0:
            n, m = n + calctabsmall[i // 3, i // 3], m + calctabsmall[i // 3, 2 - i // 3]
    if n == 18 or m == 18:
        return "tie"

    for i in range(9):
        if calctabsmall[i // 3, i // 3] == 0:
            break  # this cycle ends if any of the fields are still played
        if i == 8:
            return "tie"  # if all of the fields are finished, also the game is

    if wincounth == 3 or wincountv == 3 or wincountd == 3 or wincountd2 == 3:
        return "x"
    elif wincounth == -3 or wincountv == -3 or wincountd == -3 or wincountd2 == -3:
        return "y"
    else:
        return "senki"


root.mainloop()
