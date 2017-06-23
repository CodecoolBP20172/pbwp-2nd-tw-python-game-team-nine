from tkinter import *
import numpy as np
from random import randint
from tkinter import messagebox
import sys


calctab = np.array([[0] * 9] * 9)
calctabsmall = np.array([[0] * 3] * 3)
playfield = np.array([[" "] * 9] * 9)
playfieldsmall = np.array([[" "] * 3] * 3)


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
        if n % 3 == 2:
            print("h: ", wincounth)

        if abs(wincounth) == 3 or abs(wincountd) == 3 or abs(wincountd2) == 3:
            print("winszar")
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


while smallwincheck() == "senki":
    print(calctab)
    print(calctabsmall)
    playerturn(1)
    bigwincheck()

    # print(playfield)
    if smallwincheck() == "senki":
        print(calctab)
        print(calctabsmall)
        playerturn(2)
        bigwincheck()

    # # print(playfield)
