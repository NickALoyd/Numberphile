#https://www.youtube.com/watch?v=kC6YObu61_w
#To find happy numbers you
#Split the number into all of the digits
#square and add all the digits and repeat

#if you repeat a number it is going to be an unhappy number
#if you get to 1 then it is a happy number
def happyNumber(y):
    if y == 1: #if 1 then it terminates and is a happy number
        return True
    y = str(y) #This splits the number
    total = 0
    for i in range(len(y)):
        total += int(y[i])**2 #adds the square
    if total in visitedNumbers: #if seen before then it will just loop
        return False
    visitedNumbers.append(total) 
    return happyNumber(total)


happyNumbers = []
for i in range(100):
    visitedNumbers = []
    hNT = happyNumber(i) #happy number test
    if hNT:
        happyNumbers.append(i)
print(happyNumbers)
