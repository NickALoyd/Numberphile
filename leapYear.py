def isLeapYear(year):
    if year%400 == 0:
        return True
    if year%100 == 0:
        return False
    if year%4 == 0:
        return True
    return False

for i in range(1800,2100):
    if isLeapYear(i):
        print(i)
