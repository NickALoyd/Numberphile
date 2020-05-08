#https://www.youtube.com/watch?v=a2ey9a70yY0
def factorial(n):
    if n == 1:
        return n
    return factorial(n-1) * n
def birthdayProblem(n):
    total = 1
    for i in range(n):
        total *= ((365-i)/365)
    return total 
print(1-birthdayProblem(23))
