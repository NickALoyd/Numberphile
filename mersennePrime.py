#https://www.youtube.com/watch?v=PLL0mo5rHhk
#a mersene prime prime number that is 1 less than a square number
def isPrime(n):
    for i in range(2,int(n/2)):
        if (n%i==0):
            return False
    return True
        
for x in range(1,10):
    s = 2**x - 1
    if isPrime(s):
        print(s)
