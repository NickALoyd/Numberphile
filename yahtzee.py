#https://www.youtube.com/watch?v=fiTwar7mFws
#should be pretty close to 1296
import random

def isYahtzee():
    dice = []
    for i in range(5): dice.append(random.randint(1,6))
    return len(dice) == dice.count(dice[0])

rolls,count = 10**6,0
for i in range(rolls):
    if isYahtzee(): count += 1
print("average rolls till yahtzee",rolls/count)
