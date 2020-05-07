'''
https://www.youtube.com/watch?v=mhJY74Bw8mw
I am going to split the numbers
power the number to itself
and then add all the numbers


example
3435 = '3535'
3^3 + 4^4 + 3^3 + 5^5
= 3435

'''

def isMunchhausenNumber(n):
    s = str(n)
    total = 0
    for i in range(len(s)):
        total += int(s[i])**int(s[i])
    if total == n:
        return True
    return False

for i in range(4000):
    if isMunchhausenNumber(i): print(i)

