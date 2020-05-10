#https://www.youtube.com/watch?v=D6tINlNluuY
# There where a few that they explained in the video with the Russian Guy
#Pronic Numbers, Primary Psudo Perfect Numbers, and Harshad Numbers

def isPronic(n): #I think finding if a number is pronic is more impressive than listing them all out
    Min = int(n**(1/2))
    return Min*(Min+1) == n

def isPrime(n):
    for i in range(2,int(n/2)): 
        if (n%i==0):
            return False
    return True

def primeFac(n):
    temp,l,i = n,[],2
    while i <= (n/2)+1:
        if isPrime(temp):
            l.append(temp)
            return l
        if temp % i==0:
            temp = int(temp/i)
            l.append(i)
        else:
            i+=1    
    return l

def addInverse(l):
    total = 0
    for i in range(len(l)):
        total += (1/l[i])
    return total

def isPrimaryPsudoPerfectNumber(n):
    pf = primeFac(n)
    pf.append(n)
    i = addInverse(pf)
    return (i <= 1) & (i >=.99999) #this is sadly just an estimatie

def isHarshad(n):
    s,total = str(n), 0
    for i in range(len(s)):
        total += int(s[i])
    return n%total == 0

print(isPronic(42))
print(isPrimaryPsudoPerfectNumber(42))
print(isHarshad(42))
