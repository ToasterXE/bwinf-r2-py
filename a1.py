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
        for mitte in außenstellen:
            if not mitte == self:
                m,b,richtung = get_func(mitte.coords,self.coords)
                for stelle2 in außenstellen:
                    if not (stelle2 == self or stelle2 == mitte):
                        if b == "e":
                            if bool(stelle2.coords.x < m) == richtung:
                                self.combinations.append([mitte, stelle2])
                                # print(f"mitte {mitte.coords} stelle {self.coords} stelle2 {stelle2.coords}")
                        else:
                            if bool(stelle2.coords.x * m + b > stelle2.coords.y) == richtung:
                                self.combinations.append([mitte, stelle2])
                                # print(f"mitte {mitte.coords} stelle {self.coords} stelle2 {stelle2.coords}")
        all_combinations.append(self.combinations)

def get_distance(stelle1, stelle2):
    distance = math.sqrt((stelle1.x-stelle2.x)**2+(stelle1.y-stelle2.y)**2)

def get_strecke():
    stellen = außenstellen.copy()
    shortest = all_combinations[0]
    for combination in all_combinations:
        if len(combination)<len(shortest):
            shortest = combination
    print(shortest)
    
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