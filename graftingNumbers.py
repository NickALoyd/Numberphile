#https://www.youtube.com/watch?v=hiOMtBrH8pc
'''sqrt(x) ~ n.xm or x.n


str(98**(1/2))
remove the .'''

pos = 0 #< -  - what position you want the number to appear at

for i in range(1,10000):
    x = i**(1/2)
    sx = str(x).replace('.','') #this gets rid of the decimal point
    s = str(i)
    if sx.find(s) == pos:
        print(str(i) +": " + str(x))      
