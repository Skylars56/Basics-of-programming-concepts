import turtle
from random import randint

t1 = turtle.Turtle("turtle")
t2 = turtle.Turtle("turtle")
t1.goto(-300,100)
t2.goto(-300,-100)


for i in range(100):
    t1.forward(randint(1,50))
    t2.forward(randint(1,50))
    if t1.xcor()>300:
        turtle.write("t1 won")
        break
    if t2.xcor()>300:
        turtle.write("t2 won")
        break
    
    



turtle.done()