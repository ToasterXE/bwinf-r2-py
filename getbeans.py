daten9_longest =[]
with open("daten9.txt","r") as datei:
    for line in datei:
        if len(str(line.strip())) == 90:
            daten9_longest.append(line.strip())

liste = "["
for e in daten9_longest:
    ee = e[7:34]
    liste += ee
    liste += ", "
        # datei.write(e[7:34])
        # datei.write("\n")
with open("daten9_longeste.txt","w") as datei:
    datei.write(liste)