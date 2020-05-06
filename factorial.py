#https://www.youtube.com/watch?v=kw6l_uTakRA
def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)
print (factorial(69))
