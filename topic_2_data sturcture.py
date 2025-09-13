import turtle
import random
colors = ['blue','yellow','cyan','red','green','orange','pink','purple']
turtle_list = []
y_position = -300
for I in range(len(colors)):
    t1 = turtle.Turtle('turtle')
    t1.color(colors[I])
    t1.penup()
    t1.goto(-300,y_position)
    turtle_list.append(t1)
    y_position = y_position + 80


for I in range(100):
    for current_turtle in turtle_list:
        current_turtle.forward(random.randint(1,10))


turtle.done()


