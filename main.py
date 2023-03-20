kinosal = []
for j in range(5):
    sloupec = []
    for i in range(5):
        sloupec.append(0)
    kinosal.append(sloupec)
print(kinosal)

kinosal[2][2] = 1       #střed
for i in range(1, 4):   # čtvrtá řada
    kinosal[i][3] = 1
for i in range(5):      # poslední řada
    kinosal[i][4] = 1
print(kinosal)

sloupce = len(kinosal)
radky = 0
if sloupce:
    radky = len(kinosal[0])
for j in range(radky):
    for i in range(sloupce):
        print(kinosal[i][j], end="")
    print()

############

kinosaly = []
for i in range(5):
    kinosal = []
    for j in range(5):
        temp = []
        for k in range(5):
            temp.append(0)
        kinosal.append(temp)
    kinosaly.append(kinosal)

kinosaly[3][2][1] = 1   # Druhý kinosál, třetí řada, čtvrtý sloupec
print\
    (kinosaly)

##############

zubate = [[15, 2, 8, 5, 3],
           [3, 3, 7],
           [9, 1, 16, 13],
           [],
           [5]]
for seznam in zubate:
    for prvek in seznam:
        print(prvek, end=" ")
    print()