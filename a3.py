import math

pancakes_global = []
valid_structs = []
structmap = []
def sort(pancakes):
    global pancakes_global
    newpancakes = []
    for i in range(len(pancakes)-2,-1,-1):
        newpancakes.append(pancakes[i])
    pancakes_global = newpancakes

def sort_wbase(pancakes,base = 0):
    global pancakes_global
    if base < 0 or sorted(pancakes_global):
        pass
    else:
        newpancakes = []
        print(f"base: {base}")
        for i in range(len(pancakes)-base-2,-1,-1):
            newpancakes.append(pancakes[i])

        for i in range(len(pancakes)-base,len(pancakes)):
            newpancakes.append(pancakes[i])
        print(newpancakes)
        pancakes_global = newpancakes

def sorted(pancakes):
    previous = pancakes[-1]
    for i in range(len(pancakes)-1,-1,-1):
        current = pancakes[i]
        if current > previous:
            return False
        previous = current
    return True

class struct3():
    def __init__(self, index):
        global structmap
        old_map = structmap.copy()
        structmap[index] = "x"
        self.head = pancakes_global[index]
        self.length = 1
        self.interruption = pancakes_global[index-1]
        self.dir = False    #wird nach oben größer
        self.stapelende = len(pancakes_global) - index+2   #>1: nicht zweitunterster pancake    #0: zweitunterster pancake; +2 weil len() diff und 1 weil e nicht ende
        self.last = self.head
        if self.head > pancakes_global[index-2]:
            self.dir = True     #wird nach oben kleiner
        for i in range(index-2, 0, -1):
            if bool(self.last > pancakes_global[i]) == self.dir:
                structmap[i] = "x"
                self.length += 1
                self.last = pancakes_global[i]
            else:
                break
            
            if self.length >= 3:
                valid_structs.append(self)
            else:
                structmap = old_map

    def solve(self):
        valid_structs.remove(self)
        sort_wbase(pancakes_global)
        if self.stapelende:
            sort_wbase(pancakes_global, len(pancakes_global)-2)



class struct2():
    def __init__(self, index):
        global structmap
        old_map = structmap.copy()
        structmap[index] = "x"
        self.head = int(pancakes_global[index])
        self.length = 1
        self.interruption = pancakes_global[index+1]
        self.last = self.head
        self.dir = False
        self.stapelanfang = index      #1: nicht oberste pfannkuchen; 0: oberster pfannenkuchen
        if self.head > int(pancakes_global[index+2]):
            self.dir = True
        for i in range(index + 2, len(pancakes_global)):
            if bool(int(self.last) > int(pancakes_global[i])) == self.dir:
                structmap[i] = "x"
                self.length += 1
                self.last = pancakes_global[i]
            else:
                break
        self.extreme = min(int(self.head), int(pancakes_global[int(index + self.length)]))  #unwichtig
        # print(f"{self}self.head={self.head} dings {pancakes_global[index]}")
        print(self.extreme, self.head)
        if self.length >= 3:
            valid_structs.append(self)
            print(f"head = {self.head} len = {self.length} end = {index+self.length}")
        
        else:
            structmap = old_map


    def solve(self):
        print(pancakes_global)
        # print(f"len={len(pancakes_global)} start = {self.start}")
        
        if self.extreme == self.head:
                sort_wbase(pancakes_global,len(pancakes_global)-(self.length+2))
        if self.stapelanfang:
                sort_wbase(pancakes_global, len(pancakes_global)-1)
                self.start = 0
        sort_wbase(pancakes_global,len(pancakes_global)-1-(self.stapelanfang+1))
        valid_structs.remove(self)
        print(pancakes_global)
    
class struct1():
    def __init__(self, index):
        global structmap
        self.index = index
        self.start = int(pancakes_global[index])
        self.dir = False    #wird nach unten größer
        self.length = 1
        if self.start > int(pancakes_global[index+1]):
            self.dir = True #wird nach unten kleiner
        for i in range(index+1, len(pancakes_global)-1):
            if bool(pancakes_global[i] > pancakes_global[i+1]) == self.dir:
                self.length += 1
            else:
                break
        if self.length >= 3:
            for i in range(index,index+self.length):
                    structmap[i] = "x"
            valid_structs.append(self)

    def solve(self):
        valid_structs.remove(self)

def find_structures(pancakes):
    global structmap
    structmap = pancakes.copy()    
    for i in range(0, len(pancakes)-3):
        if structmap[i] != "x":
            struct1(i)
        print(f"structmap: {structmap}")
        # print(f"index: {i} map:{structmap}")
    for i in range(0, len(pancakes)-3):
        if structmap[i] != "x":
            struct2(i)
    print(valid_structs)


    # print(pancakes_global)
    
def getbase():
    last = int(pancakes_global[-1])
    for i in range(len(pancakes_global)-1,-1,-1):
        if int(pancakes_global[i]) > last:
            return len(pancakes_global)-i-1
        last = int(pancakes_global[i])
        bigger = 0
        e = pancakes_global[:i]
        if len(e) == 1:
            return len(pancakes_global)-1
        for ee in e:
            if pancakes_global[i] > ee:
                bigger += 1
        # print(f"bigger {bigger} i {i}")
        if bigger <= len(e)/2:
            return len(pancakes_global)-i-1
        
def main():
    with open(("pancake0.txt"),"r",encoding='utf8') as datei:
        original_size = datei.readline().strip()
        for line in datei:
            pancakes_global.append(line.strip())
    find_structures(pancakes_global)
    for structe in valid_structs:
        structe.solve()
        break
    # sort(pancakes)
    print(pancakes_global)
    while not sorted(pancakes_global):
        base = getbase()
        sort_wbase(pancakes_global, base)
        if not sorted(pancakes_global):
            find_structures(pancakes_global)
            for structe in valid_structs:
                structe.solve()
                break
    print(pancakes_global)
main()