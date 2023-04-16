import random, os
from threading import Thread

cores = os.cpu_count()
if not cores:
    cores = 4

solutions = []
pancakes_global = []
og_size = 0
solved = []
allstacks = []
pwuezahlen = [0,0,1,2,2,3,3,4,5,5]      #erstellt mit der Tabelle aus der Aufgabenstellung und den Ergebnissen von b)
fertige = []
pwue_allelösungen = []

def genstacks(len,liste, dep=0):
    for i in range(1,len+1):
        inlist = False
        for e in range(0,dep):
            if liste[e] == i:
                inlist = True
        if not inlist:
            liste[dep]=i
            if dep < len-1:
                genstacks(len,liste.copy(),dep+1)
            else:
                allstacks.append(liste)

def get_pwue(n):
    global pancakes_global, solved, solutions
    rangee = 1
    solvede = []
    pwue_last= n
    for i in range(1,n+1):
        rangee *= i
        solvede.append([])
    liste = solvede.copy()
    print("generating stacks...")
    genstacks(n,liste)
    if pwuezahlen[n-1]:
        pwue_last = pwuezahlen[n-1]
    print("calculating solutions...")
    for stacke in allstacks:
        sol = []
        pancakes_global = stacke.copy()
        for currentbest in solved:
            currentbest.clear()
        solutions.clear()


        solved = solvede.copy()
        sol.append(pancakes_global.copy())
        execute_threads(get_threads())
        sol.append(get_longest()[0])
        sol.append(get_longest()[1])

        if len(get_longest()[1])>pwue_last:
            print(f"Stapel: {pancakes_global} Stapel sortiert: {get_longest()[0]} Lösungsweg: {get_longest()[1]}")
            return 0
        
        pwue_allelösungen.append(sol)
        leerzeichen = "   " * (5-len(get_longest()[0]))
        fertige.append(f"stack: {pancakes_global} stack solved: {get_longest()[0]}{leerzeichen} solution: {get_longest()[1]}")
    
    max_moves = 0
    currentbest = 0
    print("finding longest solution")
    for solution in pwue_allelösungen:
        if len(solution[2]) > max_moves:
            max_moves = len(solution[2])
            currentbest = solution

    with open(f"daten{n}.txt","w",encoding="utf8") as output:
        for line in fertige:
            output.write(line)
            output.write("\n")
        output.write(f"Jeder Stapel der Länge {len(currentbest[0])} lässt sich in höchstens {len(currentbest[2])} Pfannkuchen-Wende-Und-Ess-Operationen sortieren.")
    print(f"Jeder Stapel der Länge {len(currentbest[0])} lässt sich in höchstens {len(currentbest[2])} Pfannkuchen-Wende-Und-Ess-Operationen sortieren.")
    print(f"Stapel: {currentbest[0]} Stapel sortiert: {currentbest[1]} Lösungsweg: {currentbest[2]}")

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
    longest = solutions[0][0]
    solution = solutions[0][1]
    for stack in solutions:
        if len(stack[0]) > len(longest):
            longest = stack[0]
            solution = stack[1]
    return(longest, solution)

def get_threads():
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
    exe_threads = []
    for data in threadlist:
        exe_threads.append(Thread(target=start_sort, args=(data,)))
    for e in exe_threads:
        e.start()
    for e in exe_threads:
        e.join()

print("Stapelgröße angeben")
stapelgröße = input()
get_pwue(stapelgröße)
input()