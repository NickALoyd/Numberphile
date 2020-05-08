#https://www.youtube.com/watch?v=5sKah3pJnHI
#https://papersizes.io/a/ Just to make sure I was right
'''
a*b = 1
a/b = 2^(1/2)
b/2=a

looking for 2 numbers that
a*b = 1
a/b = root(2)
a = root(2)*b
'''

def aSize(n):
     
    a = (2**(1/4))
    b = 1/2**(1/4)
    for i in range(n):
        temp = a
        a = b
        b = temp/2
    return a,b

for i in range(5):
    a,b = aSize(i)
    a = round(a * 1000,1)
    b = round(b * 1000,1)
    print("A" + str(i) +" paper is: " + str(b) + " x "+  str(a) + "mm")
