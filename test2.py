for k in range(9):
    for i in range(3):  # horizontal check
        wincount = 0
        for j in range(3):
            print("k: ", k, "i: ", i + (k // 3) * 3, "j: ", (j + (k % 3) * 3))


print("Ujszar")

for i in range(81):
    print("k: ", i // 9, "i: ", i // 3 - ((i // 9) * 3) + ((i // 27) * 3), "j: ",
          i - (i // 3 - ((i // 9) * 3) + ((i // 27) * 3)) * 3 - (i // 9) * 6)
