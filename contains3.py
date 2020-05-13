#https://www.youtube.com/watch?v=UfEiJJGv4CE
def contains3(n):
    return '3' in str(n)

def nextPow10(x,i):
    print(x/i)
    return 9*x + i,i*10 #This is what follows
    
x,i = 0,1
for y in range(20):
    x,i = nextPow10(x,i) #in the first 100 quintillion there is over 87% of numbers have 3s

##x = 0
##for i in range(10001):
##    if contains3(i):
##        x+=1
##    if i == 10 or i == 100 or i == 1000 or i == 10000:
##        print(str(x) + '/' +str(i) + '=' + str(x/i))
##    #1,19,271,3439 #http://oeis.org/A016189 #10**n - 9*n.




