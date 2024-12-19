#TURTLE LIBRARY
import turtle as td
import random as rd

jimmy = td.Turtle()
jimmy.shape("turtle")
jimmy.color("blue")
jimmy.fillcolor("red")
td.colormode(255)

def random_color():
    r = rd.randint(1,255)
    g = rd.randint(1,255)
    b = rd.randint(1,255)
    return (r,g,b)
    
# To Draw a square
# for i in range(4):
#     jimmy.forward(200)
#     jimmy.right(90)

# # To draw a dashed line
for _ in range(15):
    jimmy.forward(10)
    jimmy.penup() #you can also use jimmy.color("white") or jimmy.pencolor("white")
    jimmy.forward(10)
    jimmy.pendown()


# # To draw different shapes
# def draw_shape(no_sides):
#     angle = 360 / no_sides
#     for _ in range(no_sides):
#         jimmy.forward(100)
#         jimmy.right(angle)
# for side in range(3,11):
#     jimmy.color(random_color())
#     draw_shape(side)


# To draw a random walk 
# direction = [0,90,180,270]
# jimmy.pensize(15)
# jimmy.speed(10) # We can also use 'fast' ,'fastest','slow' in speed()
# for _ in range(300):
#     jimmy.color(random_color())
#     jimmy.forward(30)
#     jimmy.setheading(rd.choice(direction))








screen = td.Screen()
screen.exitonclick()