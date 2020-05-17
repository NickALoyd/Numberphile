#https://www.youtube.com/watch?v=WJ12DYBuazY&t=203s
#A sexy prime is 2 prime numbers with a diffrence of six between them
def isPrime(n):
    for i in range(2,int(n/2)): 
        if (n%i==0):
            return False
    return True

def isSexyPrime(n,a):
    a.append(n)
    if isPrime(n) and isPrime(n+6):
        return isSexyPrime(n+6,a) #a gets bigger if it has a sexy number
    return a

for i in range(2,100):
    a = isSexyPrime(i,[])
    if len(a)>1: #the len being how long the chain is
        print(a)
