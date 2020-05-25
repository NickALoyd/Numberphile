#https://www.youtube.com/watch?v=k7Gtrs9Msu8
from turtle import *

#(1) On the lower portion of a crimson cloth draw a line AB of the required length from left to right.
'''
Facts
AB == 120
AC == AB*1/3 == 160
'''

#One key point is that you don't have to measure anything
#So I think I should just use a variable instead of actual lenghts
a = 200

A = pos()   #point A
forward(a)
B = pos()   #point B

left(180)
forward(a)
right(90)
forward(a*4/3)
C = pos()   #point C

right(180)
forward(a*4/3)
right(180)
forward(a)
D = pos()   #point D

goto(B)
left(45)
forward(a)
E = pos()   #point E
setheading(180)

setx(A[0])
F = pos()   #point F
right(180)
forward(a)
G = pos()   #point G
goto(C)
#Done with shape of the flag

setheading(0)
setpos(A)
forward(a*1/4)
H = pos()   #point H
