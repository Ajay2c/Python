import turtle
from turtle import *
from turtle import Screen
import random
tur = Turtle()
scr = Screen()
ran = random
colors = ["Alice Blue", "Antique White", "Aqua", "Aquamarine", "Beige", "Bisque", "Blue Violet", "Cadet Blue"]
direction = [0, 90, 180, 270]
tur.shape("turtle")
tur.pensize(2)
tur.speed(9)
turtle.colormode(255)
def random_color():
    r = ran.randint(0, 255)
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)
    tup = (r, g, b)
    return tup

def draw_random():
    tur.color(random_color())
    tur.forward(10)
    tur.setheading(ran.choices(direction))

for i in range(3,11):
    draw_random()
