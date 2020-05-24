#https://www.youtube.com/watch?v=fiTwar7mFws
#should be pretty close to 1296
import random

def isYahtzee():
    dice = []
    for i in range(5): dice.append(random.randint(1,6))
    return len(dice) == dice.count(dice[0])

rolls = 0
while not isYahtzee(): rolls += 1
print("It took ", rolls," to get a yahtzee.")
