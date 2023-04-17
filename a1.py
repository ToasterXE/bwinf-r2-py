import pygame, math
außenstellen = []
all_combinations = []
class außenstelle():
    def __init__(self,coords):
        x,y = coords.split()
        self.coords = pygame.math.Vector2(float(x),float(y))
        außenstellen.append(self)
        self.combinations = []
    def get_combinations(self):
        for stelle1 in außenstellen:
            if not stelle1 == self:
                m,b,richtung = get_func(self.coords,stelle1.coords)
                for stelle2 in außenstellen:
                    if not (stelle2 == self or stelle2 == stelle1):
                        if b == "e":
                            if bool(stelle2.coords.x < m) == richtung:
                                self.combinations.append([stelle1, self, stelle2])
                                # print(f"mitte {self.coords} stelle {stelle1.coords} stelle2 {stelle2.coords}")
                        else:
                            if bool(stelle2.coords.x * m + b > stelle2.coords.y) == richtung:
                                self.combinations.append([stelle1, self, stelle2])
                                # print(f"mitte {self.coords} stelle {stelle1.coords} stelle2 {stelle2.coords}")
        all_combinations.append(self)

def get_distance(stelle1, stelle2):
    distance = math.sqrt((stelle1.x-stelle2.x)**2+(stelle1.y-stelle2.y)**2)
globalsol = 0
found = False
def try_strecke(startpunkt,alle,reihenfolge):
    global found
    if found:
        return(1)
    reihenfolge.append(startpunkt[0])
    if startpunkt[0] in alle:
        alle.remove(startpunkt[0])   
    else:
        print(startpunkt[0].coords.x,startpunkt[0].coords.y,"e")

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

def get_strecke():
    stellen = außenstellen.copy()
    reihenfolge = []
    shortest = all_combinations[0]
    for punkt in all_combinations:
        if not found:
            # print(len(punkt.combinations))
            # if len(punkt.combinations)<len(shortest.combinations):
            shortest = punkt
            # print(shortest.coords)
            for i in range(0, len(shortest.combinations)):
                
                r = try_strecke(shortest.combinations[i], stellen.copy(), reihenfolge.copy())
                if r:
                    for i in range(0,len(globalsol)):
                        print(globalsol[i].coords.x, globalsol[i].coords.y)
                    break

    
def get_func(mitte, stelle1):   #zone in der sich e befinden darf
    neue_stelle = mitte + pygame.math.Vector2(stelle1.y - mitte.y, (stelle1.x - mitte.x) * -1)
    if mitte.y-neue_stelle.y and mitte.x-neue_stelle.x:
        m = (mitte.y - neue_stelle.y) / (mitte.x-neue_stelle.x)
    else:
        m = mitte.x
        richtung = bool(stelle1.x > mitte.x)    #true: zone ist rechts von der linie, false: zone ist links von der linie
        return(m,"e",richtung)
    b = mitte.y - (mitte.x*m)
    richtung = bool(stelle1.x*m-b > stelle1.y)  #true: zone ist unter der linie, false: zone ist über der linie
    # print(mitte, neue_stelle, m, b)
    return(m,b,richtung)

ymitte = 0
xmitte = 0
def main():
    global ymitte, xmitte
    x_ee = []
    y_ee = []
    with open(str("wenigerkrumm1.txt"),"r",encoding='utf8') as datei:
        for line in datei:
            x,y = line.strip().split()
            x_ee.append(float(x))
            y_ee.append(float(y))
            außenstelle(line.strip())
    ybiggest = max(y_ee)
    xbiggest = max(x_ee)
    ysmallest = min(y_ee)
    xsmallest = min(x_ee)
    ymitte = (ybiggest - ysmallest) / 2
    xmitte = (xbiggest-xsmallest) / 2
    for stelle in außenstellen:
        stelle.get_combinations()
    get_strecke()
main()