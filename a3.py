import math

pancakes_global = []
valid_structs = []

def sort(pancakes):
    global pancakes_global
    newpancakes = []
    for i in range(len(pancakes)-2,-1,-1):
        newpancakes.append(pancakes[i])
    pancakes_global = newpancakes

def sort_wbase(pancakes,base = 0):
    global pancakes_global
    newpancakes = []
    print(base)
    for i in range(len(pancakes)-base-2,-1,-1):
        newpancakes.append(pancakes[i])

    for i in range(base-2,len(pancakes)):
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
        self.dir = False
        self.start = index
        if self.head > pancakes_global[index+2]:
            self.dir = True
        for i in range(index + 2, len(pancakes_global)):
            if bool(self.last > pancakes_global[i]) == self.dir:
                structmap[i] = "x"
                self.length += 1
                self.last = pancakes_global[i]
            else:
                break
        print(f"head = {self.head} len = {self.length} index = {index+self.length}")
        self.extreme = min(int(self.head), int(pancakes_global[int(index + self.length)]))
        if self.length >= 3:
            valid_structs.append(self)

    def solve(self):
        print(pancakes_global)
        print(f"len={len(pancakes_global)} start = {self.start}")
        sort_wbase(pancakes_global,len(pancakes_global)-1-(self.start+1))
        print(pancakes_global)

def find_structures(pancakes):
    structmap = pancakes.copy()
    for i in range(0, len(pancakes)-3):
        if structmap[i] != "x":
            struct(i, structmap)
    print(valid_structs)
    for structe in valid_structs:
        structe.solve()
    # print(pancakes)
    # sort(pancakes)
    # print(pancakes_global)

    # sort_wbase(pancakes,4)
    # print(pancakes_global)
    
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