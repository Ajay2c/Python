# import turtle_game
# print(turtle_game.ajay_size)

from turtle import Turtle, Screen
# example is: car = CarBluePrint()

# Object = Class(BluePrint)
timmy = Turtle()  # timmy- Object , Turtle()- method
timmy.shape("turtle")
timmy.color("red", "green")
timmy.forward(100)

my_screen = Screen()

# example is: car.speed
# object.attributes
print(my_screen.canvheight)
my_screen.exitonclick()
