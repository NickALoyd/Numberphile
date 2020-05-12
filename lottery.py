#https://www.youtube.com/watch?v=U7f8j3mVMbc
import random

def runLottery(chosenNumbers):
    win,balls = [],[ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,
                    11,12,13,14,15,16,17,18,19,20,
                    21,22,23,24,25,26,27,28,29,30,
                    31,32,33,34,35,36,37,38,39,40,
                    41,42,43,44,45,46,47,48,49]        
    for i in range(6):
        x = random.choice(balls)
        if not x in chosenNumbers:
            return False
        win.append(x)
        balls.remove(x) #so you can't draw it again
    print(win) #if all of them where in the chosen Numbers
    return True #then it is a winning ticket

winningNumbers = [14,19,31,33,34,45]

for x in range(1,13983816):
        if runLottery(winningNumbers):
            print(str(x) + " Winner Winner Chicken Dinner!")
        if not x%1000000: print("mill")
