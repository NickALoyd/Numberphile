from turtle import *
import nepalGeometry as ng


length = 200
LOOKATME = ng.Point(1,2)
print(LOOKATME)


A = ng.Point(pos())
forward(length)

B = ng.Point(pos())
goto(A.getPos())
setheading(90)
forward(length)

D = ng.Point(pos())
forward(length*1/3)

C = ng.Point(pos())
goto(D.getPos())
goto(B.getPos())
#we going going to want an intersection between a circle and a line

lBD = B+D
setheading(lBD.facingTo()) #Facing D
left(180)
forward(length)

E = ng.Point(pos())
F = ng.Point(0,E.y)
G = ng.Point(length,E.y)

goto(F.getPos()) 
goto(G.getPos())
goto(C.getPos())
goto(A.getPos())

setheading(0)
forward(length/4)
H = ng.Point(pos())

lCG = C+G
lHI = ng.Line(H,ng.Point(H.x,H.y+1))


I = lCG + lHI
goto(I.getPos())


#Bisect CF at point J


lCF = C+F
J = lCF.midpoint()
lJK = ng.Line(J,ng.Point(J.x + 1,J.y))
K = lCG+lJK
goto(C.getPos())
goto(J.getPos())
goto(K.getPos())

L = lHI+lJK

goto(G.getPos())
goto(J.getPos())


lJG = J+G
M = lHI+lJG
goto(M.getPos())


rM_BD = ng.findShortestPointOfLinePoint(lBD,M,0,length/4)
setheading(270)
forward(rM_BD)

N = ng.Point(pos())
goto(M.getPos())
O = ng.Point(0,M.y)
goto(O.getPos())

lLN = L+N


cL = ng.Circle(lLN.distance(),L)
lOP = ng.Line(O,ng.Point(O.x +1,O.y))
print(ng.intersectionsOfLineCircle(lOP,cL))
P,Q = ng.intersectionsOfLineCircle(lOP,cL)
goto(N.getPos())
left(90)

print(pos()[0])
print(P.y)
circle(lLN.distance(),136/2)
circle(lLN.distance(),-136)

lMQ = ng.Line(M,Q)
cM = ng.Circle(lMQ.distance(),M)
goto(P.getPos())
setheading(270)
circle(lMQ.distance(),360/2)
print(Q.getPos())
print(pos())

goto(Q.getPos())
goto(M.getPos())
done()

