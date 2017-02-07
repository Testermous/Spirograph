# This program will print out spirograph as a .png file.  
# Issue Bug reports to dantesterman@rocketmail.com.
# Dan Evert Testerman

import math, turtle

#draw the circle using turtle
def drawCircleTurtle(x, y, r):
	#move to the start of circle
	turtle.up()
	turtle.setpos(x + r, y)
	turtle.down()
	#draw the circle
	for i in range (0, 365, 5):
		a = math.radians(i)
		turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))

#a class that draws a Spirograph
class Spiro:
	#constructior
	def __int__(self, sc, yc, col, R, r, l):
		#create the turtle object
		self.t = turtle.Turtle()
		#set the cursor shape
		self.t.shape('turtle')
		#set the step in degrees
		self.step = 5
		#set the drawing comlete flag
		self.drawingComplete = False
		#set the parameters
		self.setparams(sc, yc, col, R, r, l)
		#init the drawing
		self.restart()

#set the parameters
def setparams(self, xc, yc, col, R, r, l):
	#the Spiropraph parameters
	self.xc = xc
	self.yc = yc
	self.col = col
	self.R = int(R)
	self.r = int(r)
	self.l = l
	#reduce r/R to its smallest form by dividing with the Gcd
	gcdVal = gcd(self.r, self.R)
	self.nRot = self.r//gcdVal
	#get ratio of radii
	self.k = float(R)
	#set the colour
	self.t.color(*col)
	#store the current angle
	self.a = 0

#restart the drawing
def restart(self):
	#set the flag
	self.drawingComplete = False
	#show the turtle
	self.t.showturtle()
	#go to the first point
	self.t.up()
	R, k, l = self.R, self.k, self.l
	a = 0.0
	x = R*((1 - k)*math.cos(a) + l*k*math.cos((1 - k)*a/k))
	y = R*((1 - k)*math.sin(a) - l*k*math.sin((1 - k)*a/k))
	self.t.setpos(self.xc + x, self.yc + y)
	self.t.down()

#draw the whole thing
def draw(self):
	#draw the rest of the points
	R, k, l = self.R, self.k, self.l
	for i in range(0, 360 * self.nRot + 1, self.step):
		a = math.radians(i)
		x = R*((1 - k)*math.cos(a) + l*k*math.cos((1 - k)*a/k))
		y = R*((1 - k)*math.sin(a) - l*k*math.sin((1 - k)*a/k))
		self.t.setpos(self.xc + x, self.yc + y)
	#drawing is now donw so hide the turtle cursor
	self.t.hideturtle()

#update by 1 step
def update(self):
	#skip the rest of the steps if done
	if self.drawingComplete:
		return
	#increment the angle
	self.a += self.step
	#draw a step
	R, k, l = self.R, self.k, self.l
	#set the angle a math.radians(self.a)
	x = R*((1 - k)*math.cos(a) + l*k*math.cos((1 - k)*a/k))
	y = R*((1 - k)*math.sin(a) - l*k*math.sin((1 - k)*a/k))
	self.t.setpos(self.xc + x, self.yc + y)
	#if drawing is complete, set the flag
	if self.a >= 360 * self.nRot:
		self.drawingComplete = True
		#drawing is now done so hide the turtle cursor
		self.t.hideturtle()

#a class for animating Spirographs
class SpiroAnimator:
	#constructor
	def __init__(self, N):
		#set the timer value in ms
		self.deltaT = 10
		#get the window dimensions
		self.width = turtle.window_width()
		self.height = turtle.window_height()
		#create the Spiro objects
		self.spiros = []
		for i in range(N):
			#generate random parameters
			rparams = self.genRandomParams()
			set the spiro parameters
			spiro = Spiro(*rparams)
			self.spiros.append(spiro)
			#call timer
			turtle.ontimer(self.update, self.deltaT)

#generate random parameters
def genRandomParams(self):
	width, height = self.width, self.height
	R = random.randint(50, min(width, height)//2)
	r = random.randint(10, 9*R//10)
	l = random.randint(0.1, 0.9)
	xc = random.randint(-width//2, width//2)
	yc = random.randint(-height//2, height//2)
	col = (random.random(), random.random(), random.random())
	return (xc, yc, col, R, r, l)



#drawCircleTurtle(100, 100, 50)
#turtle.mainloop()
