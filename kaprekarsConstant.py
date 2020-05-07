#https://www.youtube.com/watch?v=d8TRcZklX_Q

9281 #starting number
9821 #sort from largest to smallest
1289 #sort from smallest to largest
d = 8532 #b-c
e = 8532 #plug into step a
#if a == e return*/


def intToList(a):
    s = str(a)
    x = []
    for i in range(len(s)):
        x.append(int(s[i]))
    return x

def sortHightoLow(a):
    return sorted(a,reverse = True)
    
def sortLowtoHigh(a):
    return sorted(a)

def listToInt(a):
    total = 0
    for i in range(len(a)):
        total += a[i]*10**(len(a)-i-1)
    return total

    return a[0]*1000 + a[1]*100 + a[2]*10 + a[3]*1 #find a better way of saying this

def getTo6174(a): #yay recursion
    b = intToList(a)
    c = sortHightoLow(b)
    d = sortLowtoHigh(b)
    e = listToInt(c) - listToInt(d)
    print(a)
    if a == e:
        return e
    else:
        return getTo6174(e)


print(getTo6174(2984))


