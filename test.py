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
        if bigger < len(e)/2:
            return len(pancakes_global)-i-1
        
pancakes_global = ['4', '1', '3', '5', '6']
print(getbase())