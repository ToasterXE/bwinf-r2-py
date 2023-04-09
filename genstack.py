import random
len = 6
e = []
for i in range(0,len):
    ee = random.randint(1,len)
    while ee in e:
        ee = random.randint(1,len)
    print(ee)
    e.append(ee)