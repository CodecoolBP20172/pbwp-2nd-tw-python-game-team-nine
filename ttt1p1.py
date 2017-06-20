from tkinter import *
import numpy as np
from random import randint
from tkinter import messagebox
import sys

root = Tk()
root.title("Tic Tac Toe v1.1")
# root.geometry("625x575")
playfield = np.array([[" "] * 3] * 3)
calctab = np.array([[0] * 3] * 3)
bclick = True

if len(sys.argv) > 1:
    if sys.argv[1] == "m":
        single = False
else:
    single = True

buttons = []
for i in range(81):
    btn = Button(root, text="", font=("Arial 30 bold"), height=1, width=2, command=lambda i=i: ttt(i))
    btn.grid(row=int(i / 9), column=i % 9, sticky=S + N + E + W)
    buttons.append(btn)

restartButton = Button(root, text=("Restart"), font=("Arial 30 bold"), height=1, width=2, command=lambda: restart())
restartButton.grid(row=9, columnspan=9, sticky=S + N + E + W)


def restart():
    if wincheck() == "o" or wincheck() == "x" or wincheck() == "tie":
        for i in range(3):
            for j in range(3):
                calctab[i, j] = 0
                playfield[i, j] = " "
        for i in range(9):
            buttons[i]["text"] = ""


def wincheck():

    playerwins = False
    if playerwins == False:
        for i in range(3):  # horizontal check
            wincount = 0
            for j in range(3):
                wincount = wincount + calctab[i, j]
            if wincount == 3 or wincount == -3:
                playerwins = True
                # print("wincheck1")
            if playerwins:
                break

    if playerwins == False:
        for i in range(3):  # vertical check
            wincount = 0
            for j in range(3):
                wincount = wincount + calctab[j, i]
            if wincount == 3 or wincount == -3:
                playerwins = True
                # print("wincheck2")
            if playerwins:
                break
            # print(wincount)

    if playerwins == False:
        wincount = 0
        for i in range(3):  # diagonal check
            wincount = wincount + calctab[i, i]
        if wincount == 3 or wincount == -3:
            playerwins = True
            # print("wincheck3")
        # print(wincount)

    if playerwins == False:
        wincount = 0
        for i in range(3):  # other diagonal check
            wincount = wincount + calctab[i, 2 - i]
        if wincount == 3 or wincount == -3:
            playerwins = True
            # print("wincheck4")
        # print(wincount)

    if playerwins == False:
        lofasz = False
        n = 0
        for i in range(3):
            for j in range(3):
                if calctab[i, j] == 0:
                    n = n + 1
        if n == 0:
            lofasz = True

    if wincount == 3:
        return "x"
    elif wincount == -3:
        return "o"
    elif lofasz:
        return "tie"
    else:
        return "wincheck"


def AI_check():
    twopoints = False

    if twopoints == False:
        for i in range(3):  # horizontal win check
            pointcount = 0
            for j in range(3):
                pointcount = pointcount + calctab[i, j]
            if pointcount == -2:
                twopoints = True
                for k in range(3):
                    if calctab[i, k] == 0:
                        rownumber = i
                        colnumber = k
                        break
                break

    if twopoints == False:
        for i in range(3):  # vertical win check
            pointcount = 0
            for j in range(3):
                pointcount = pointcount + calctab[j, i]
            if pointcount == -2:
                twopoints = True
                for k in range(3):
                    if calctab[k, i] == 0:
                        rownumber = k
                        colnumber = i
                        break
                break

    if twopoints == False:
        pointcount = 0
        for i in range(3):  # diagonal win check
            pointcount = pointcount + calctab[i, i]
        if pointcount == -2:
            twopoints = True
            for i in range(3):
                if calctab[i, i] == 0:
                    rownumber = i
                    colnumber = i

    if twopoints == False:
        pointcount = 0
        for i in range(3):  # other diagonal win check
            pointcount = pointcount + calctab[i, 2 - i]
        if pointcount == -2:
            twopoints = True
            for i in range(3):
                if calctab[i, 2 - i] == 0:
                    rownumber = i
                    colnumber = 2 - i

    if twopoints == False:
        for i in range(3):  # horizontal playerwin check
            pointcount = 0
            for j in range(3):
                pointcount = pointcount + calctab[i, j]
            if pointcount == 2:
                twopoints = True
                for k in range(3):
                    if calctab[i, k] == 0:
                        rownumber = i
                        colnumber = k
                        break
                break

    if twopoints == False:
        for i in range(3):  # vertical playerwin check
            pointcount = 0
            for j in range(3):
                pointcount = pointcount + calctab[j, i]
            if pointcount == 2:
                twopoints = True
                for k in range(3):
                    if calctab[k, i] == 0:
                        rownumber = k
                        colnumber = i
                        break
                break

    if twopoints == False:
        pointcount = 0
        for i in range(3):  # diagonal playerwin check
            pointcount = pointcount + calctab[i, i]
        if pointcount == 2:
            twopoints = True
            for i in range(3):
                if calctab[i, i] == 0:
                    rownumber = i
                    colnumber = i

    if twopoints == False:
        pointcount = 0
        for i in range(3):  # other diagonal playerwin check
            pointcount = pointcount + calctab[i, 2 - i]
        if pointcount == 2:
            twopoints = True
            for i in range(3):
                if calctab[i, 2 - i] == 0:
                    rownumber = i
                    colnumber = 2 - i

    if twopoints:
        return [rownumber, colnumber]
    else:
        return [-1, -1]


def ttt(i):
    if wincheck() == "wincheck":
        global bclick
        if buttons[i]["text"] == "" and bclick:  # player 1 click
            buttons[i]["text"] = "X"
            if single == False:
                bclick = False
            # return i + 10
            i = i + 10
            print(i)
        elif buttons[i]["text"] == "" and bclick == False and single == False:  # player 2 click
            buttons[i]["text"] = "O"
            bclick = True
            # return i + 10
            i = i + 20
            print(i)
        player = i // 10
        print(player)
        move = i - (player * 10)
        print(move)
        print(calctab)
        c = 0
        for i in range(3):
            for j in range(3):
                c = c + calctab[i, j]
        print("C: " + str(c))

        n = 0
        for i in range(3):
            for j in range(3):
                if move == n and player == 1:
                    playfield[i, j] = "x"
                    calctab[i, j] = 1
                elif move == n and player == 2:
                    playfield[i, j] = "o"
                    calctab[i, j] = -1
                n = n + 1
        print(calctab)
        d = 0
        for i in range(3):
            for j in range(3):
                d = d + calctab[i, j]
        print("d: " + str(d))

        print(calctab)
        print(playfield)
    if wincheck() == "wincheck" and single and not c == d:  # AI move
        if AI_check() == [-1, -1]:
            AIMoved = False
            if calctab[1, 1] == 0:
                playfield[1, 1] = "o"
                calctab[1, 1] = -1
                if buttons[4]["text"] == "":
                    buttons[4]["text"] = "O"
                    AIMoved = True
            while AIMoved == False:
                print("aimoves")
                i = randint(0, 2)
                j = randint(0, 2)
                coord = i * 3 + j
                if calctab[i, j] == 0:
                    playfield[i, j] = "o"
                    calctab[i, j] = -1
                    buttons[coord]["text"] = "O"
                    AIMoved = True
        else:
            list = AI_check()
            playfield[list[0], list[1]] = "o"
            calctab[list[0], list[1]] = -1
            coord = list[0] * 3 + list[1]
            buttons[coord]["text"] = "O"

        # for i in range(3):
        #     for j in range(3):
        #         if playfield[i,j]=="x":
        #             calctab[i,j]=1
        #         if playfield[i,j]=="o":
        #             calctab[i,j]=-1
        print(calctab)
        print(playfield)

    if wincheck() == "x":
        print("Player one wins!")
        # messageWindowX()
        messagebox.showinfo("Result", "Player One wins!")

    elif wincheck() == "o":
        print("Player two wins!")
        # messageWindowO()
        messagebox.showinfo("Result", "Player Two wins!")

    elif wincheck() == "tie":
        print("Tie")
        # messageWindowO()
        messagebox.showinfo("Result", "Tie!")


root.mainloop()
