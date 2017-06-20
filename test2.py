for k in range(9):
    for i in range(3):  # horizontal check
        wincount = 0
        for j in range(3):
            print("k: ", k, "i: ", i+(k//3)*3, "j: ", (j+(k%3)*3))