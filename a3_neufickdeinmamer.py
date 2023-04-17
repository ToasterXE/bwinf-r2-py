import random, os, time, sys
from threading import Thread

cores = os.cpu_count()
if not cores:
    cores = 4

solutions = []
pancakes_global = []
og_size = 5
solved = []
allstacks = []
pwuezahlen = [0,0,1,2,2,3,3,4,5,5]
def genstacks(len,liste, dep=0):
    for i in range(1,len+1):
        ee = False
        for e in range(0,dep):
            if liste[e] == i:
                ee = True
        if not ee:
            liste[dep]=i
            if dep < len-1:
                genstacks(len,liste.copy(),dep+1)
            else:
                allstacks.append(liste)

fertige = []
insgsol = []
pwue = False
def get_pwue(n):
    global pancakes_global, solved, solutions
    rangee = 1
    pwue = True
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
    for stacke in allstacks:
        sol = []
        pancakes_global = stacke.copy()
        for e in solved:
            e.clear()
        solutions.clear()


        solved = solvede.copy()
        sol.append(pancakes_global.copy())
        execute_threads(get_threads())
        sol.append(get_longest()[0])
        sol.append(get_longest()[1])

        if len(get_longest()[1])>pwue_last:
            print(f"Jeder Stapel der Länge {n} lässt sich in höchstens {len(get_longest()[1])} Pfannkuchen-Wende-Und-Ess-Operationen sortieren.")
            print(f"Stapel: {pancakes_global} Stapel sortiert: {get_longest()[0]} Lösungsweg: {get_longest()[1]}")
            return 0
        
        insgsol.append(sol)
        e = "   " * (5-len(get_longest()[0]))
        fertige.append(f"stack: {pancakes_global} stack solved: {get_longest()[0]}{e} solution: {get_longest()[1]}")
        print(f"stack: {pancakes_global} stack solved: {get_longest()[0]}{e} solution: {get_longest()[1]}")   #hiererer
    max_moves = 0
    e = 0


    for solution in insgsol:
        if len(solution[2]) > max_moves:
            max_moves = len(solution[2])
            e = solution

    with open(f"daten{n}.txt","w",encoding="utf8") as output:
        for line in fertige:
            output.write(line)
            output.write("\n")
        output.write(f"Jeder Stapel der Länge {len(e[0])} lässt sich in höchstens {len(e[2])} Pfannkuchen-Wende-Und-Ess-Operationen sortieren.")
    print(f"Jeder Stapel der Länge {len(e[0])} lässt sich in höchstens {len(e[2])} Pfannkuchen-Wende-Und-Ess-Operationen sortieren.")
    print(f"Stapel: {e[0]} Stapel sortiert: {e[1]} Lösungsweg: {e[2]}")
counter = 0

def sort(pancakes,base = 0,lösungsweg=["eee"]):
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

def normalize(stack):
    ostack = stack.copy()
    nstack= stack.copy()
    for i in range(0,len(stack)):
        max_e = max(ostack)
        index = stack.index(max_e)
        ostack[index] = 0
        nstack[index] = len(stack)-i
    return nstack
   #es gibt mehr lösungswege als lösungen; lösungswege rechnet man aus mit get_numofsolutions()
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
    # print("counting pancake stacks...")
    longest = solutions[0][0]
    solution = solutions[0][1]
    for stack in solutions:
        if len(stack[0]) > len(longest):
            longest = stack[0]
            solution = stack[1]
    return(longest, solution)


def get_threads():
    if not pwue:
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
    if not pwue:
        print("executing threads...")
    exe_threads = []
    for data in threadlist:
        exe_threads.append(Thread(target=start_sort, args=(data,)))
    for e in exe_threads:
        e.start()
    if not pwue: 
        print("eating pancakes...")
    for e in exe_threads:
        e.join()

# main()

get_pwue(5)
# print(normalize([8, 2, 11]))
# print(sorted(['1', '11', '4', '5', '7', '9']))
# print(get_numofsolutions(5))
# print(counter)