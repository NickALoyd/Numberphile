#https://www.youtube.com/watch?v=RxxDD2LWAyY
#A lucky number is a number where you delete the nth number of the list
#Ehh I don't really know how to explain it

NS = list(range(1,1000,1)) #Better way to make lists
def deleteNth(NS,n):
    del NS[n-1::n] #Fancy deleting list making

for i in [1] + list(range(1,100)): # I don't like the range why 100? Cuz it's big 
    deleteNth(NS,NS[i])
print(NS)
