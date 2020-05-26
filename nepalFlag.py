#https://www.youtube.com/watch?v=k7Gtrs9Msu8
from turtle import *
import math
import numpy
#(1) On the lower portion of a crimson cloth draw a line AB of the required length from left to right.
'''
Facts
AB == 120
AC == AB*1/3 == 160
'''

def angleOf(x,y):
    magU = (x[0]**2 + x[1]**2)**(1/2)
    print("(should be 5) magU: ", magU)
    magV = (y[0]**2 + y[1]**2)**(1/2)
    print("(should be sqrt(34)) magV: ", magV)
    dotP = (x[0]*y[0]) + (x[1]*y[1])
    #dotP = (x[0]*x[1]) + (y[0]*y[1])
    print("(should be 27) dp: ", dotP)

    cost = dotP/(magU*magV)
    theta = math.acos(cost)
    deg = math.degrees(theta)
        
    print(deg)
    return deg #returns in degrees'''

x,y = [0,10],[4,5]

def angleOf(x,y):
    #assumes x is at zero
    print(x)
    print(y)
    theta = (y[1]-x[1])/(y[0]-x[0])
    return math.degrees(math.atan(theta)) + 360
    
print(angleOf(x,y))

def slope(p1,p2):
    return ((p2[1]-p1[1])/(p2[0]-p1[0]))

def b(p1,p2):
    s = slope(p1,p2)
    return p1[1] - (s*p1[0])

def shortestPoint(line,point):
    ls = slope(line[0],line[1]) #lines slope
    lb = b(line[0],line[1])     #lines y-Intercept
    ps = -1/ls                  #points slope
    pb = point[1] - (ps*point[0]) #points y-Intercept
    px = (pb-lb)/(ls-ps)        #value for x 
    return (px,ls*px + lb)      #shortest point

def distancePoints(p1,p2):
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**(1/2)
            
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

setpos(C)
setheading(angleOf(C,G))

while pos()[0] < H[0]:
    forward(1)
I = pos()   #point I
setheading(270)
goto(H)
print(F)
print(C)
J = (0,(F[1] + C[1])/2) #point J
goto(J)
setheading(0)
forward(a/2)
K = pos()   #point K
goto(G)
goto(J)

setheading(angleOf(J,K))
while pos()[0] < H[0]:
    forward(1)
L = pos()
goto(J)
setheading(angleOf(J,G))
while pos()[0] < H[0]:
    forward(.1)
M = pos()   #point M

p1 = shortestPoint((D,B),M)
d1 = distancePoints(p1,M) #this distance is the radius of M
setheading(270)
forward(d1)
N = pos()   #point N

O = (0,M[1])


#N to L is the distance for the radius of the circle
left(90)
while pos()[1] < M[1]:
    circle(L[1]-N[1], -1)
Q = pos()   #point P
circle(L[1]-N[1], 1)
while pos()[1] < M[1]:
    circle(L[1]-N[1], 1)
P = pos()   #point P


goto(M)
setheading(270)
d2 = distancePoints(M,Q)
forward(d2)
left(90)

circle(d2, -1)
while pos()[1] < M[1]:
    circle(d2, -1)
circle(d2, 1)
while pos()[1] < M[1]:
    circle(d2, 1)
