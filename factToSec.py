#https://www.youtube.com/watch?v=kUBIJdGsD1A
#Just the fact that 10! = 42 days exactly
def factorail(n):
    if n == 1: return n
    return n*factorail(n-1)
def secToDays(s): return s/60/60/24

x = factorail(10)
print(secToDays(x))
