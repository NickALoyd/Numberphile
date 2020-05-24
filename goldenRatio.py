#https://www.youtube.com/watch?v=mqK63v2Jzks&t=243s
'''
golden ratio
(a+b)/a = a/b
'''
c = 100
phi = 0
for a in range(1,1000):
    for b in range(1,1000):
        temp = abs(((a+b)/a) - (a/b))
        if c > temp:
            c = temp
            phi=a/b
print(phi)
