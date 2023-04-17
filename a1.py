import pygame, math
außenstellen = []
class außenstelle():
    def __init__(self,coords):
        x,y = coords.split()
        self.coords = pygame.math.Vector2(float(x),float(y))
        außenstellen.append(self)
        self.combinations = []

    def get_combinations(self):
        for pos1 in außenstellen:
            if not pos1 == self:
                m,b,richtung = get_func(self.coords,pos1.coords)
                for pos2 in außenstellen:
                    if not (pos2 == self or pos2 == pos1):
                        if b == "x":
                            if bool(pos2.coords.x < m) == richtung:
                                self.combinations.append([pos1, self, pos2])
                                # print(f"mitte {self.coords} stelle {stelle1.coords} stelle2 {stelle2.coords}")
                        elif b == "y":
                            if bool(pos2.coords.y > m) == richtung:
                                self.combinations.append([pos1, self, pos2])
                                # print(f"mitte {self.coords} stelle {stelle1.coords} stelle2 {stelle2.coords}")
                        else:
                            if bool(pos2.coords.x * m + b > pos2.coords.y) == richtung:
                                self.combinations.append([pos1, self, pos2])
                                # print(f"mitte {self.coords} stelle {stelle1.coords} stelle2 {stelle2.coords}")

def get_distance(pos1, pos2):
    return math.sqrt((pos1.x-pos2.x)**2+(pos1.y-pos2.y)**2)
globalsol = 0
found = False
def try_strecke(startpunkt,alle,reihenfolge):
    global found
    if found:
        return 1
    reihenfolge.append(startpunkt[0])
    if startpunkt[0] in alle:
        alle.remove(startpunkt[0])   

    if len(alle) == 2:
        reihenfolge.append(startpunkt[1])
        reihenfolge.append(startpunkt[2])
        found = True
        global globalsol
        globalsol = reihenfolge.copy()

    for i in range(0,len(startpunkt[2].combinations)):
        e = startpunkt[2].combinations[i]

        if e[0] == startpunkt[1] and e[2] in alle:
            try_strecke(e,alle.copy(),reihenfolge.copy())

ausgeschlossen = []

def get_strecke():
    punkte = außenstellen.copy()
    reihenfolge = []
    for punkt in außenstellen:
        if not found:
            for i in range(0, len(punkt.combinations)):     
                if not (found or punkt.combinations[i] in ausgeschlossen):
                    reihenfolge_solved = try_strecke(punkt.combinations[i], punkte.copy(), reihenfolge.copy())
                    if reihenfolge_solved:
                        break
                    ausgeschlossen.append(punkt.combinations[i].reverse())
    
def get_func(mitte, pos1):
    neue_pos = mitte + pygame.math.Vector2(pos1.y - mitte.y, (pos1.x - mitte.x) * -1)
    if mitte.y-neue_pos.y and mitte.x-neue_pos.x:
        m = (mitte.y - neue_pos.y) / (mitte.x-neue_pos.x)
    elif mitte.y-neue_pos.y:
        m = mitte.x
        richtung = bool(pos1.x > mitte.x)    #true: zone ist rechts von der linie, false: zone ist links von der linie
        return(m,"x",richtung)
    else:
        m = mitte.y
        richtung = bool(pos1.y < mitte.y)    #true: zone ist unter der linie, false: zone ist über der linie
        return(m, "y", richtung)
    b = mitte.y - (mitte.x*m)
    richtung = bool(pos1.x*m+b < pos1.y)  #true: zone ist unter der linie, false: zone ist über der linie
    return(m,b,richtung)

def main():
    x_ee = []
    y_ee = []
    with open(str(dateiname),"r",encoding='utf8') as datei:
        for line in datei:
            x,y = line.strip().split()
            x_ee.append(float(x))
            y_ee.append(float(y))
            außenstelle(line.strip())
    for stelle in außenstellen:
        stelle.get_combinations()
    get_strecke()
    if found:
        länge = 0
        with open(str(dateiname).replace(".txt","output.txt"),"w", encoding="utf8") as datei:
            for i in range(0,len(globalsol)):
                if i < len(globalsol)-1:
                    länge += get_distance(globalsol[i].coords,globalsol[i+1].coords)
                datei.write(f"{i}: {globalsol[i].coords.x} {globalsol[i].coords.y}")
                datei.write("\n")
            datei.write(f"Die Länge der Strecke beträgt {länge}m.") #Einheit der Strecke nicht bekannt
    else:
        print("Es konnte keine passende Strecke gefunden werden.")
print("Dateiname angeben:")
dateiname = input()
main()
print("Weg gefunden")
input()