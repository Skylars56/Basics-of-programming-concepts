import turtle
import funs

colors = [    "red","blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "brown"]
t1 = turtle.Turtle('turtle')
t2 = turtle.Turtle('turtle')
t2.speed(1000000000000000000000000000000)
t2.color('red')

t1.forward(100)
# funs.make_square(t1,100)
# funs.make_square(t1,50)
# funs.make_square(t2,300)

# funs.make_star(t1,35)
# funs.make_star(t2,50)
funs.make_graph(t2,1000,145,colors)


turtle.done()

