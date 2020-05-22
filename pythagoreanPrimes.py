#https://www.youtube.com/watch?v=yu_aqA7mw7E

pythagoreanPrimes = []

def isPrime(n):
    for i in range(2,int(n/2)+1):
        if not n%i:
            return False
    return True

def isPathagoreanPrime(n):
    if isPrime(n): #n has to be a prime
        for a in range(1,int(n**(1/2))): #the max a can be is sqrt(n)
            b = (n-(a**2))**(1/2) #a**2 + b**2 = n solve for b    b=sqrt(n-a**2)  
            if b > 0 and int(b) == b: #checks b isn't imaginary first and it is an int
                return True
    return False

for i in range(1000):
    if isPathagoreanPrime(i):
        pythagoreanPrimes.append(i)
print(pythagoreanPrimes)
