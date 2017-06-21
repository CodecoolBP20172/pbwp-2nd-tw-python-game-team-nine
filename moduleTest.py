from tkinter import *
import numpy as np
from random import randint
from tkinter import messagebox
import sys

calctab = np.array([[0] * 9] * 9)

playfield = np.array([[" "] * 9] * 9)

# for i in range(9):
#     for j in range(9):
#         calctab[i, j] = randint(-1, 1)

# print(calctab)


def wincheck():
    playerwins = False
    if playerwins is False:
        k, i = None, None
        x, y = k, i
        o = 0
        for n in range(81):
            if n % 3 == 0:
                wincounth, wincountv, wincountd, wincountd2 = 0, 0, 0, 0
            k = n // 9
            i = n // 3 - ((n // 9) * 3) + ((n // 27) * 3)
            j = n - (n // 3 - ((n // 9) * 3) + ((n // 27) * 3)) * 3 - (n // 9) * 6
            wincounth = wincounth + calctab[i, j]
            wincountv = wincountv + calctab[j, i]
            if k != x or i % 3 == 0:
                o = o + 1
                x, y = k, i
                wincountd = wincountd + calctab[i + n % 3, j]
                wincountd2 = wincountd2 + calctab[i + n % 3, n // 9 * 3 + abs(j % 3 - 2) - n // 27 * 9]
                if n % 3 == 2:
                    print("n: ", n, "d: ", wincountd, "d2: ", wincountd2, "k: ", k)

            if abs(wincounth) == 3 or abs(wincountv) == 3 or abs(wincountd) == 3 or abs(wincountd2) == 3:
                playerwins = True
                print("lofasz")
                break

    if wincounth == 3 or wincountv == 3 or wincountd == 3 or wincountd2 == 3:
        return "x"
    elif wincounth == -3 or wincountv == -3 or wincountd == -3 or wincountd2 == -3:
        return "o"
    else:
        return "senki"


def playerturn(player):
    move = int(input("Player " + str(player) + " moves to:"))
    n = 0
    for i in range(9):
        for j in range(9):
            n = n + 1
            if move == n and player == 1:
                playfield[i, j] = "x"
            elif move == n and player == 2:
                playfield[i, j] = "o"

    for i in range(9):
        for j in range(9):
            if playfield[i, j] == "x":
                calctab[i, j] = 1
            if playfield[i, j] == "o":
                calctab[i, j] = -1


while wincheck() == "senki":
    print(calctab)
    playerturn(1)
    # print(playfield)
    if wincheck() == "senki":
        print(calctab)
        playerturn(2)
        # print(playfield)
