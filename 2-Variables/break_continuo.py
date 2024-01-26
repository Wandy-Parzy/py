c = 0

while c < 10:
    c += 1
    print(c)
    if c == 5:
        print("Sigue continue")
       # break
        continue
    print("despues continue")
else:
    print("Fin")