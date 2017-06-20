import numpy as np
playfield = np.array([["      "]*3]*3)
calctab = np.array([[0]*3]*3)

def wincheck():

    playerwins=False
    if playerwins == False:
        for i in range(3): #horizontal check
            wincount=0
            for j in range(3):
                wincount = wincount + calctab[i,j]
            if wincount == 3 or wincount == -3:
                playerwins = True
                #print("wincheck1")
            break

    if playerwins == False:
        for i in range(3): #vertical check
            wincount=0
            for j in range(3):
                wincount = wincount + calctab[j,i]
            if wincount == 3 or wincount == -3:
                playerwins = True
                #print("wincheck2")
            break
            # print(wincount)

    if playerwins == False:
        wincount=0
        for i in range(3): #diagonal check
            wincount = wincount + calctab[i,i]
        if wincount == 3 or wincount == -3:
            playerwins = True
            #print("wincheck3")
        # print(wincount)

    if playerwins == False:
        wincount=0
        for i in range(3): #other diagonal check
            wincount = wincount + calctab[i,2-i]
        if wincount == 3 or wincount == -3:
            playerwins = True
            #print("wincheck4")
        # print(wincount)


    if wincount == 3:
        return "x"
    elif wincount == -3:
        return "o"
    else:
        return ""





def playerturn(player):
    move = int(input("Player " + str(player) +" moves to:"))
    n=0
    for i in range(3):
        for j in range(3):
            n=n+1
            if move==n and player == 1:
                playfield[i,j] ="x"
            elif move==n and player == 2:
                playfield[i,j]="o"

    for i in range(3):
        for j in range(3):
            if playfield[i,j]=="x":
                calctab[i,j]=1
            if playfield[i,j]=="o":
                calctab[i,j]=-1



while wincheck()=="":
    playerturn(1)
    print(playfield)
    print(wincheck())
    if wincheck()=="":
        playerturn(2)
        print(playfield)
        print(wincheck())


if wincheck()=="x":
    print("Player one wins!")
elif wincheck()=="o":
    print("Player two wins!")
