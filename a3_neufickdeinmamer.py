import math
import random, os, time, sys
from threading import Thread

cores = os.cpu_count()
if not cores:
    cores = 4

solutions = []
pancakes_global = []
og_size = 0
solved = []

def genstack(len):
    stack = []
    for i in range(0,len):
        pancake = random.randint(1,len)
        while pancake in stack:
            pancake = random.randint(1,len)
        stack.append(pancake)

counter = 0
def sort(pancakes,base = 0,liste=0):
    global counter, solutions
    counter += 1
    # if counter == numofsolution//10:
    #     print("10%...")
    newpancakes = []
    # print(f"base: {base}")
    for i in range(len(pancakes)-base-2,-1,-1):
        newpancakes.append(pancakes[i])

    for i in range(len(pancakes)-base,len(pancakes)):
        newpancakes.append(pancakes[i])
    if sorted(newpancakes)and len(newpancakes)>1:
        solved[len(pancakes)].append(normalize(pancakes))
        # print(f"sorted {newpancakes} schritte: {liste}")
        solutions.append([newpancakes,liste])
    return(newpancakes)

def sorted(pancakes):
    previous = int(pancakes[-1])
    for i in range(len(pancakes)-1,-1,-1):
        current = int(pancakes[i])
        if current > previous:
            return False
        previous = current  
    # print(solved)
    
    return True

def normalize(stack):
    ostack = stack.copy()
    nstack= stack.copy()
    for i in range(0,len(stack)):
        max_e = max(ostack)
        index = stack.index(max_e)
        ostack[index] = 0
        nstack[index] = len(stack)-i
    return nstack


def recurse(stack,liste):   #es gibt mehr lösungswege als lösungen; lösungswege rechnet man aus mit get_numofsolutions()
    estack = normalize(stack)
    if not solved[len(stack)]:
        for i in range(0, len(stack)):
            if not solved[len(stack)]:
                lister = liste.copy()
                lister.append(i)
                nstack = stack.copy()
                nstack = sort(nstack,i,lister)
                # print(f"stack:{stack}nstack:{nstack}")
                if len(nstack)>1:
                    recurse(nstack,lister)
 
def start_sort(startdata):
    for start in startdata:
        pancakes = pancakes_global.copy()
        pancakes = sort(pancakes,start-1)
        recurse(pancakes,[start-1])

def get_longest():
    print("counting pancake stacks...")
    longest = solutions[0][0]
    solution = solutions[0][1]
    for stack in solutions:
        if len(stack[0]) > len(longest):
            longest = stack[0]
            solution = stack[1]
    return(longest, solution)

def main():
    global og_size,pancakes_global
    with open(("pancake0.txt"),"r",encoding='utf8') as datei:
        og_size = int(datei.readline().strip())
        for line in datei:
            pancakes_global.append(int(line.strip()))
            solved.append([])

    print("calculating time...")
    print(f"estimated time: {calculate_etime()}")
    execute_threads(get_threads())
    print(get_longest())

def get_numofsolutions(size):
    numofsolutions = 0
    for i in range(2, size+1):
        new = 1
        for e in range(i,size+1):
            new *= e
        numofsolutions += new 

    return numofsolutions
    

def get_threads():
    print("creating threads...")
    threads = []
    for i in range(0,og_size):
        if i >= cores:
            threads[i%cores].append(i+1)
        else:
            threads.append([i+1])
    return threads

def execute_threads(threadlist):
    print("executing threads...")
    exe_threads = []
    for data in threadlist:
        exe_threads.append(Thread(target=start_sort, args=(data,)))
    for e in exe_threads:
        e.start()
    print("eating pancakes...")
    for e in exe_threads:
        e.join()

def calculate_etime():
    starttime = time.time()
    for i in range(0,1000000):
        sort(pancakes_global.copy(),random.randint(0,og_size))
    endtime = time.time()
    etime100 = endtime-starttime
    etime = (etime100 * get_numofsolutions(og_size)) / 1000000
    return f"{etime//60}m {int(etime%60)}s"
numofsolution = get_numofsolutions(og_size)
main()
# print(normalize([8, 2, 11]))
# print(sorted(['1', '11', '4', '5', '7', '9']))
# print(get_numofsolutions(5))
# print(counter)