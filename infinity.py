#https://www.youtube.com/watch?v=elvOZm0d4H0
#just making the list of the infinities up to a certian number

MAX = 10
print(list(range(1,MAX)))

allInts = [0]
l = lambda x:(x,-x)
for i in range(1,MAX):allInts += l(i)
print(allInts)

allFracs = []
for i in range(MAX):
    for n in range(i,0,-1):
        allFracs.append(str(n) + "/" + str(i-n+1)) #determine what d is
print(allFracs)
