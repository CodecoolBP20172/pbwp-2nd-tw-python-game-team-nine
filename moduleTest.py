from tkinter import *
import numpy as np
from random import randint
from tkinter import messagebox
import sys

calctab = np.array([[0] * 9] * 9)
print(calctab)
playfield = np.array([[" "]*9]*9)

def wincheck():
    playerwins=False
    if playerwins == False:
        for k in range(9):
            for i in range(3):  # horizontal check
                wincount = 0
                for j in range(3):
                    wincount = wincount + calctab[i+(k//3)*3][j+(k%3)*3]
                if wincount == 3 or wincount == -3:
                    playerwins = True
                    # print("wincheck1")
                if playerwins:
                    break
                print(wincount)


    if wincount == 3:
        return "x"
    elif wincount == -3:
        return "o"
    else:
        return "senki"


def playerturn(player):
    move = int(input("Player " + str(player) +" moves to:"))
    n=0
    for i in range(9):
        for j in range(9):
            n=n+1
            if move==n and player == 1:
                playfield[i,j] ="x"
            elif move==n and player == 2:
                playfield[i,j]="o"

    for i in range(9):
        for j in range(9):
            if playfield[i,j]=="x":
                calctab[i,j]=1
            if playfield[i,j]=="o":
                calctab[i,j]=-1

while True:
    playerturn(1)
    print(playfield)
    print(calctab)
    print(wincheck())
    if wincheck() =="senki":
        playerturn(2)
        print(playfield)
        print(wincheck())
        print(calctab)
