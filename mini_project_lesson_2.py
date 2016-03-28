import turtle


#writes initials of my name E and N

def draw_myname():
    brad = turtle.Turtle()
    # for letter E  
    brad.left(180)
    brad.forward(100)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(100)
    brad.pu()
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.pd()
    brad.forward(100)
    brad.pu()
    brad.setpos(0,0)
    brad.pd()
    #reset the turtle position
    brad.right(180)
    brad.pu()
    brad.forward(25)
    brad.pd()
    #for the letter N
    brad.left(90)
    brad.forward(200)
    brad.right(135)
    brad.forward(1.44*200)
    brad.left(135)
    brad.forward(200)

    
draw_myname()
