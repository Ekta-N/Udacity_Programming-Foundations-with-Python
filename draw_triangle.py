import turtle

def draw_triangle():
    brad = turtle.Turtle()
    window = turtle.Screen()
    for i in range(0,3):
        brad.forward(100)
        brad.right(120)
    window.exitonclick()

draw_triangle()
