#https://www.youtube.com/watch?v=4aMtJ-V26Z4
#split the digits, square the numbers, add up the squares and you get the origninal number

a = 153         #startingNumber
b = "153"       #stringify
c = [1,5,3]     #listify
d = [1,125,27]  #squareList
e = 153         #addList

def stringify(a):
    return str(a)

def listify(a):
    b = []
    for i in range(len(a)):
        b.append(int(a[i]))
    return b

def cubeList(a):
    for i in range(len(a)):
        a[i] = a[i]**(len(a))
    return a
    

def addList(a):
    total = 0
    for i in range(len(a)):
        total += a[i]
    return total

def isNarcissistic(a):
    b = stringify(a)
    b = listify(b)
    b = cubeList(b)
    b = addList(b)
    if a == b:
        return True
    else:
        return False

a = []
for i in range(1,10000):
    if (isNarcissistic(i)):
        print(i)
