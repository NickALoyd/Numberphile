#https://www.youtube.com/watch?v=bFfSfzjhfC8
'''
In this video we are trying to see how many flips until heads is pulled 14 times in a row

should be around 32766 flips
'''

import random

def coinFlip():
    if random.randint(0, 1) == 0:
        return 'H'
    return 'T'

def run32766Times():
    outcome = '' #This is the list of heads or tails outcomes
    for i in range(32766):
        outcome += coinFlip() #flips 32766 coins
    maxHeads = 0
    #what is better practice
    #for i in range(100): #This looks more readable but it dosn't need to test zero
    for i in range(1,100): #extremely rare this will need anything over 20 but just in case
        temp = i*'H'
        if temp in outcome:
            maxHeads = i
    return maxHeads


for y in range(10):
    x = []
    for i in range(100):
        x.append(run32766Times())
    print(sum(x)/len(x)) #This should print a value close to 14
    
    
