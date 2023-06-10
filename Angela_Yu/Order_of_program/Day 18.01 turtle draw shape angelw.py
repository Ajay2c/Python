from turtle import Turtle, Screen
import random
tim = Turtle()
scr = Screen()
ran = random

color_list = ["black", "blue", "pink", "yellow", "red"]
def draw_sapes(shapes):
    shape_size = round(360 / shapes)
    for shape in range(shapes):
        tim.forward(100)
        tim.right(shape_size)
        tim.forward(100)

for i in range(3, 11):
    tim.color(ran.choices(color_list))
    draw_sapes(i)

scr.exitonclick()