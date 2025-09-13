import turtle
import random

color = "pink"
shape = "turtle"

t1 = turtle.Turtle()
t1.shape(shape)
t1.color("red")
t1.shapesize(1,1)
t1.forward(100)
# t1.left(90) 
t1.penup()
t1.goto(-300,50)

t2 = turtle.Turtle()
t2.shape(shape)
t2.color("blue")
t2.shapesize(1,1)
t2.penup()
t2.forward(100)
t2.goto(-300,-50)

for i in range(100):
    t1.forward(random.randint(1,10))
    t2.forward(random.randint(1,10))







turtle.done()