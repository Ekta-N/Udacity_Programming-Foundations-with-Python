import turtle

def draw_sq(somett):
        for i in range(0,4):
            somett.forward(100)
            somett.right(90)     
        
    
   
def draw():
    brad = turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor("red")
    brad.speed(2)
    brad.color("yellow")
    brad.pensize(5)
    brad.shape("circle")
    brad.pencolor("brown")
    draw_sq(brad)
    brad.circle(100)
    brad.forward(100)
    for i in range(0,3):
        brad.forward(100)
        brad.right(120)
    window.exitonclick()
    
draw()
