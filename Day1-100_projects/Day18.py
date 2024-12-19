import colorgram as cg
import turtle as td
import random as rd



jimmy = td.Turtle()

color_list = cg.extract("D:\code_python\Day1-100_projects\image.jpg", 80)
color_palette = []
print(color_list)

for count in color_list:
    rgb = count.rgb
    
    color_palette.append((rgb.r , rgb.g, rgb.b))

color = rd.choice(color_palette)

screen = td.Screen()
screen.exitonclick()
