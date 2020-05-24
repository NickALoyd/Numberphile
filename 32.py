#https://www.youtube.com/watch?v=EJRXWNWJOrQ
def magicTrick():
    i = input("Enter an int between 1-9: ")
    if i.isdigit() and len(i)==1 and i != "0":
        s = 0
        i *= 3 # makes "1" to "111"
        for x in range(len(i)): s += int(i[x])
        print(i[0],"+",i[1],"+",i[2],"=",s)
        print(i,"/",s,"=",int(i)/s)
    else:
        return magicTrick()
magicTrick()
