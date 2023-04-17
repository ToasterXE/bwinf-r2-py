import pygame, math
außenstellen = []
class außenstelle():
    def __init__(self,coords):
        x,y = coords.split()
        self.coords = pygame.math.Vector2(float(x),float(y))
        außenstellen.append(self)
        self.combinations = []
    def get_combinations(self):
        for stelle1 in außenstellen:
            if not stelle1 == self:
                m,b,richtung = get_func(stelle1.coords,self.coords)
                for stelle2 in außenstelle:
                    if not stelle2 == self:
                        if bool(stelle2.coords.x * m + b <= stelle2.coords.y) == richtung:
                            self.combinations.append([stelle1, stelle2])
        print(self.combinations)

def get_distance(stelle1, stelle2):
    distance = math.sqrt((stelle1.x-stelle2.x)**2+(stelle1.y-stelle2.y)**2)

# def get_inzone(mitte, stelle1, stelle2):    #prüft ob stelle2 in zone von stelle zwei-mitte ist


def get_func(mitte, stelle1):   #zone in der sich e befinden darf
    neue_stelle = mitte + pygame.math.Vector2(stelle1.y - mitte.y, (stelle1.x - mitte.x) * -1)
    m = (mitte.y - neue_stelle.y) / (mitte.x-neue_stelle.x)
    b = mitte.y - (mitte.x*m)
    richtung = bool(stelle1.x*m-b > stelle1.y)  #true: zone ist unter der linie, false: zone ist über der linie
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
    außenstellen[0].get_combinations()
main()