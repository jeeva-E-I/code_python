import turtle as td
import random as rd

jimmy = td.Turtle()
jimmy.shape("turtle")
td.colormode(255)

def random_color():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    return (r, g, b)
jimmy.speed("fastest")
def draw_spirograph(size):
    for _ in range(int(360 / size)):
        jimmy.color(random_color())
        jimmy.circle(100)
        jimmy.setheading(jimmy.heading() + size)
        

draw_spirograph(5)


screen = td.Screen()
screen.exitonclick()