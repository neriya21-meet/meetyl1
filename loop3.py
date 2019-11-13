from turtle import Turtle
import turtle
class Ball(Turtle):
	def __init__(self,name,color,r,dx,dy,shape):
		Turtle.__init__(self)
		self.name=name
		self.color=color
		self.r=r/10
		self.dx=dx
		self.dy=dy
		self.penup()
		self.shape()
	
	def move(self):
		current_x=self.xcor()
		new_x=self.xcor()+self.xcor()
		current_y=self.ycor()
		new_y=self.ycor()+self.ycor()
		right_side_ball=new_x+r/10
		left_side_ball=new_x+r/10
		up_side_ball=new_y+r/10
		down_side_bal=new_y+r/10


		print(self.name + " Is bouncing ")



turtle.shape("circle")

Ball1=Ball("Mikey","pink",30,10,10,turtle.penup(),"circle")


