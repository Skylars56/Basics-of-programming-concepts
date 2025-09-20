import turtle 

class MyOwnTurtle:
    def __init__(self,pox,poy,color,size=1):
        self.tt = turtle.Turtle()
        self.tt.shape("turtle")
        self.tt.penup()
        self.tt.goto(pox,poy)
        self.tt.color(color)
        self.tt.shapesize(size,size)
            
    

t1 = MyOwnTurtle(0,100,"red",5)
t2 = MyOwnTurtle(100,50,"blue",2)






turtle.done()

