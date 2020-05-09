#https://www.youtube.com/watch?v=aTSYARnB-3Y
#A magic square has all the diaginols, verticles, and horizontals add up to the same number

def isMagicSquare(grid):
    size = len(grid)
    l = []
    
    for x in range(size):   #vertical
        total = 0
        for y in range(size):
            total += grid[y][x]
        l.append(total)
    
    for x in range(size):   #horizontal
        total = 0
        for y in range(size):
            total += grid[x][y]
        l.append(total)
    
    total = 0
    for x in range(size):   #diagonal upperleft to lowwerright
            total += grid[x][x]
    l.append(total)

    total = 0
    for x in range(size):   #diagonal inverted
            total += grid[x][size-1-x]
    l.append(total)

    if l.count(l[0]) == len(l):     #if all same return true
        return True
    return False

def printSquare(grid):
    size = len(grid)
    l = []
    for x in range(size):
        print(grid[x])
    print()

x= [[11,22,58,85],
    [55,88,12,21],
    [82,51,25,18],
    [28,15,81,52]]
print(isMagicSquare(x))    
