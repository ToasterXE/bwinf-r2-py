import random, os
from threading import Thread

cores = os.cpu_count()
if not cores:
    cores = 4

solutions = []
pancakes_global = []
og_size = 0
solved = []

def sort(pancakes,base = 0,lösungsweg=[]):
    global solutions
    newpancakes = []
    for i in range(len(pancakes)-base-2,-1,-1):
        newpancakes.append(pancakes[i])

    for i in range(len(pancakes)-base,len(pancakes)):
        newpancakes.append(pancakes[i])
    if sorted(newpancakes)and len(newpancakes)>1:
        solved[len(pancakes)-1].append((pancakes))
        solutions.append([newpancakes,lösungsweg])
    return(newpancakes)

def sorted(pancakes):
    previous = int(pancakes[-1])
    for i in range(len(pancakes)-1,-1,-1):
        current = int(pancakes[i])
        if current > previous:
            return False
        previous = current   
    return True

def sort_stack(stack,lösungsweg):
    if not solved[len(stack)]:
        for i in range(0, len(stack)):
            if not solved[len(stack)]:
                lösungsweg_copy = lösungsweg.copy()
                lösungsweg_copy.append(i)
                nstack = stack.copy()
                nstack = sort(nstack,i,lösungsweg_copy)
                if len(nstack)>1:
                    sort_stack(nstack,lösungsweg_copy)
 
def start_sort(startdata):
    for start in startdata:
        pancakes = pancakes_global.copy()
        pancakes = sort(pancakes,start,[start])
        sort_stack(pancakes,[start])

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
    with open((dateiname),"r",encoding='utf8') as datei:
        og_size = int(datei.readline().strip())
        for line in datei:
            pancakes_global.append(int(line.strip()))
            solved.append([])

    execute_threads(get_threads())
    print(f"sortierter Stapel: {get_longest()[0]} Lösungsweg: {get_longest()[1]}")

def get_threads():
    print("creating threads...")
    if sorted(pancakes_global):
        solved[len(pancakes_global)-1].append((pancakes_global))
        solutions.append([pancakes_global,[None]])
    threads = []
    for i in range(0,og_size):
        if i >= cores:
            threads[i%cores].append(i)
        else:
            threads.append([i])
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

print("Dateinamen angeben:")
dateiname = input()

main()
input()