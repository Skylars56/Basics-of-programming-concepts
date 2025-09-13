def bmi(w,h):
    w = w/2.20652 # conver to kg
    # write you height
    h = h/39.37

    bmi = w/(h**2)

    if bmi <18.5:
        print("you are under weight")
    elif bmi >18.5 and bmi < 24.9:
        print("healthy weight")
    elif bmi >24.9:
        print("overweight")
    print(bmi)




def avg(x,y):
    V = (x+y)/2
    return V




def make_square(tt,steps,angle=90,running_time=4):
    for i in range(running_time):
        tt.forward(steps)
        tt.left(angle)


# 5 times forward and turn 144 degrees

def make_star(tt,steps):
    for i in range(5):
        tt.forward(steps)
        tt.left(144)




def make_graph(tt,size,ang,clist):
    for i in range(0,size):
        tt.color(clist[i%len(clist)])
        tt.forward(i)
        tt.left(ang)
    


