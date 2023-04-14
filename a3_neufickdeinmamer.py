import math
import random, os
from threading import Thread

cores = os.cpu_count()
if not cores:
    cores = 4

pancakes_global = []
og_size = 0

def genstack(len):
    stack = []
    for i in range(0,len):
        pancake = random.randint(1,len)
        while pancake in stack:
            pancake = random.randint(1,len)
        stack.append(pancake)

counter = 0
def sort(pancakes,base = 0):
    global counter
    counter += 1
    newpancakes = []
    # print(f"base: {base}")
    for i in range(len(pancakes)-base-2,-1,-1):
        newpancakes.append(pancakes[i])

    for i in range(len(pancakes)-base,len(pancakes)):
        newpancakes.append(pancakes[i])
    
    if sorted(newpancakes)and len(newpancakes)>1:
        pass
        # print(f"sorted {newpancakes}")
    return(newpancakes)

def sorted(pancakes):
    previous = pancakes[-1]
    for i in range(len(pancakes)-1,-1,-1):
        current = pancakes[i]
        if current > previous:
            return False
        previous = current
    return True


def recurse(stack):   #es gibt mehr lösungswege als lösungen; lösungswege rechnet man aus mit
    for i in range(0, len(stack)):
        nstack = stack.copy()
        nstack = sort(nstack,i)
        print(f"stack:{stack}nstack:{nstack}")
        if len(nstack)>1:
            recurse(nstack)
 

def beans(startdata):
    for start in startdata:
        pancakes = pancakes_global.copy()
        pancakes = sort(pancakes,start-1)
        print(counter)
        recurse(pancakes)


def main():
    global og_size
    with open(("pancake0.txt"),"r",encoding='utf8') as datei:
        og_size = int(datei.readline().strip())
        for line in datei:
            pancakes_global.append(line.strip())
    execute_threads(get_threads())

def get_numofsolutions(size):
    numofsolutions = 0
    for i in range(2, size+1):
        new = 1
        for e in range(i,size+1):
            new *= e
        numofsolutions += new 

    return numofsolutions
    
def get_threads():
    threads = []
    for i in range(0,og_size):
        if i >= cores:
            threads[i%cores].append(i+1)
        else:
            threads.append([i+1])
    return threads

def execute_threads(threadlist):
    exe_threads = []
    for data in threadlist:
        exe_threads.append(Thread(target=beans, args=(data,)))
    for e in exe_threads:
        e.start()
    for e in exe_threads:
        e.join()
# main()
print(get_numofsolutions(5))
# print(counter)