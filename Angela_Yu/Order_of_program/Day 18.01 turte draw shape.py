import turtle
from turtle import Turtle, Screen
from random import Random

color_list = ["black", "blue", "pink", "yellow", "red"]

ran = Random()
turtle = Turtle()
scren = Screen()
turtle.shape("turtle")


shapes = {
    "triangle": 3,
    "square" : 4,
    "pentagon" : 5,
    "hexagon" : 6,
    "octagon" : 7,

}
for s in shapes:
    turtle.color(ran.choices(color_list))
    print(shapes[s])
    total_sides = shapes[s]
    sides_angle = 360 / total_sides
    for i in range(total_sides):
        turtle.forward(100)
        turtle.right(sides_angle)
        turtle.forward(100)


scren.exitonclick()