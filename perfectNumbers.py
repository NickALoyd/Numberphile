'''
    Get all of the factors
    add up to see if it equals the original number
    if so it's perfect
'''
def perfectNumbers(x):
    factors = []
    for i in range(int(x/2)):
        if (x%(i+1) == 0):
            factors.append(i+1)
    #at this point we should have all factors except for itself
    y = 0
    for i in range(len(factors)):
        y += factors[i]

    if (x == y):
        print( str(x) + " is a Perfect Numbers")
    else:
        print(str(x) + " is Not a perfect number")

perfectNumbers(496)
