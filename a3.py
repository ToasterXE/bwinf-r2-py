import math

pancakes_global = []
valid_structs = []

def sort(pancakes):
    global pancakes_global
    newpancakes = []
    for i in range(len(pancakes)-2,-1,-1):
        newpancakes.append(pancakes[i])
    pancakes_global = newpancakes

def sorted(pancakes):
    previous = pancakes[-1]
    for i in range(len(pancakes)-1,-1,-1):
        current = pancakes[i]
        if current > previous:
            return False
        previous = current
    return True

class struct():
    def __init__(self, index, structmap):
        structmap[index] = "x"
        self.head = pancakes_global[index]
        self.length = 1
        self.interruption = pancakes_global[index+1]
        self.last = self.head
        if self.head > pancakes_global[index+2]:
            self.dir = True
        else:
            self.dir = False
        for i in range(index + 2, len(pancakes_global)):
            if bool(self.last > pancakes_global[i]) == self.dir:
                self.length += 1
                self.last = pancakes_global[i]
            else:
                break
        self.extreme = min(int(self.head), int(pancakes_global[self.head + self.length]))
        if 
        if self.length >= 3:
            valid_structs.append(self)

    

def find_structures(pancakes):
    structmap = pancakes.copy()
    for i in range(0, len(pancakes)-3):
        if structmap[i] != "x":
            struct(i, structmap)
    print(valid_structs)

def main():
    with open(("pancake0.txt"),"r",encoding='utf8') as datei:
        original_size = datei.readline().strip()
        for line in datei:
            pancakes_global.append(line.strip())
    find_structures(pancakes_global)
    #while not sorted(pancakes_global):
    #    sort(pancakes_global)
    #print(pancakes_global)
main()