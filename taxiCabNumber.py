#https://www.youtube.com/watch?v=LzjaDKVC4iY
#a number that can be represented as 2 cubes in 2 diffrent ways
def isTaxiCab(goal):
    Max = int(goal**(1/3)) + 1
    l = []
    for x in range(1,Max):        
        for y in range(int((goal-x**3)**(1/3)),Max):
            if x**3 + y**3 == goal:
                l.append([x,y])
    if len(l) >= 4:
        print(l[0:int(len(l)/2)])
        return True
    return False
    
goal = 1729

for i in range(1,100000):
    if isTaxiCab(i):
        print(i)
