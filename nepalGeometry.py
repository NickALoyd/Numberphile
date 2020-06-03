#https://www.xarg.org/2016/07/calculate-the-intersection-points-of-two-circles/
import math
import numpy as np


class Point():
	def __init__(self, x,y=None):
		if y == None:
			self.x = float(x[0])
			self.y = float(x[1])
		else:
			self.x = x
			self.y = y

	def getPos(self):
		return (self.x,self.y)

class Circle():
	def __init__(self,radius,center):
		self.r = radius
		self.center = center
		self.x = self.center.x
		self.y = self.center.y

class Line():
	def __init__(self,p1,p2):
		self.p1 = p1
		self.p2 = p2

	def slope(self):
		if self.p2.x-self.p1.x == 0:
			return None
		return (self.p2.y-self.p1.y)/(self.p2.x-self.p1.x)

	def yInter(self):
		if self.slope() == None: #check if on a y 
			if not self.p1.x: return "AR" #all points are true
			else: return None #its a parellel line
		return self.p1.y - (self.slope() * self.p1.x)

	def xInter(self):
		if self.slope() == None:
			return self.p1.x
		if not self.slope():#parellel line to x axis
			if not self.p1.y: return "AR" #all points are true
			else: return None 
		return - self.yInter() * (1/(self.slope()))

	def getYof(self,x): #y = mx+b
		return self.slope() * x + self.yInter()
	def getXof(self,y): #mx = y-b
		return y - self.yInter()


	def distance(self):
		a = self.p1.x - self.p2.x
		b = self.p1.y - self.p2.y
		return (a**2 + b**2)**(1.0/2.0)

	def facingTo(self):
		if math.degrees(math.atan(self.slope())) == None:
			return 90
		return math.degrees(math.atan(self.slope()))	

	def midpoint(self):
		x = (self.p1.x + self.p2.x)/2.0
		y = (self.p1.y + self.p2.y)/2.0
		return x,y

def hypotenuse(A,B):
		return (A**2 + B**2)**(1.0/2.0) 

def intersectionOf2Circles(A,B):
	d = hypotenuse(B.x - A.x, B.y - A.y)
	if (d <= A.r + B.r and d >= abs(B.r - A.r)):
		ex = (B.x - A.x) / d
		ey = (B.y - A.y) / d
		x = (A.r * A.r - B.r * B.r + d * d) / (2 * d)
		y = (A.r * A.r - x * x)**(1.0/2.0)
		P1 = (A.x + x * ex - y * ey,
		A.y + x * ey + y * ex)
		P2 = (A.x + x * ex + y * ey,
		A.y + x * ey - y * ex)
		return (P1,P2)
	return "NONE" # No Intersection, far outside or one circle within the other'''

def intersectionOf2Lines(A,B):
	#I need to solve this when slopes are vertical
	if A.slope() == None:
		#if slope A has a vertical and the other is normal
		#print("Case 1: ")
		x = A.p1.x
		y = B.slope() * x + B.yInter()
		return x,y

	if B.slope() == None:
		#print("Case 2: ")
		x = B.p1.x
		y = A.slope() * x + A.yInter()
		return x,y

	#print("Case 3: ")
	x = (B.yInter() - A.yInter())/(A.slope() - B.slope())
	y = A.slope() * x + A.yInter()
	return x,y


def findShortestPointOfLinePoint(l,p, min, max):
	smallestDistance = 10**100
	shortestPos = 0
	for i in np.arange(min,max, .001): 
		x = i
		y = x*l.slope() + l.yInter()
		d = Line(p, Point([x,y])).distance()
		
		if (d < smallestDistance):
			smallestDistance = d
			shortestPos= x,y
	print(shortestPos)
	return smallestDistance

def quadradicFormula(a,b,c):
	p1 = (-b + (b**2 - 4*a*c)**(1.0/2.0))/(2*a)
	p2 = (-b - (b**2 - 4*a*c)**(1.0/2.0))/(2*a)
	return p1,p2

def intersectionsOfLineCircle(l,c):
	#(x+h)**2 + (y+k)**2 = r**2, y = s*x+b  wolframalpha plot of a circle, and plot of line
	h,k,r = c.x,c.y,c.r
	s,b = l.slope(),l.yInter()
	print("h,k,r,s,b",h,k,r,s,b)

	p1x = -(-h - k*s - b*s - (-k**2 - 2*k*b - b**2 + r**2 + 2*h*k*s + 2*h*b*s - h**2*s**2 + r**2*s**2)**(1.0/2.0))/(1 + s**2)
	p1y = l.getYof(p1x)

	p2x = -(-h - b*s - k*s + (-b**2 - 2*b*k - k**2 + r**2 + 2*b*h*s + 2*h*k*s - h**2*s**2 + r**2*s**2)**(1.0/2.0))/(1 + s**2)
	p2y = l.getYof(p2x)

	return (p1x,p1y),(p2x,p2y)
	
p1 = Point([0,0])
p2 = Point([1,2])
l = Line(p1,p2)
c = Circle(4,Point([2,7]))

print(intersectionsOfLineCircle(l,c))
