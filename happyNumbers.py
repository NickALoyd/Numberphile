#happy numbers
#https://www.youtube.com/watch?v=kC6YObu61_w
'''
    Rules of happy numbers
    Split number into x digits
    square each digit then add up

    if terminate to 1 happy number
    if repeated unhappy number
'''
def happyNumbers(x):
    if x == 1:
        return ("Happy")    
    strX = str(x)
    xSquared = []
    for i in range(len(strX)):
        xSquared.append(int(strX[0+i:1+i])**2)    
    x = xSquared
    total = 0
    for i in range(len(x)):
        total += x[i]
    print (total)
    return happyNumbers(total)
x = 97
print(happyNumbers(x))
