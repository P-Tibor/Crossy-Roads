import turtle
from turtle import Turtle
import random
turtle.colormode(255)


class Car(Turtle):

    def __init__(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        super(Car, self).__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(r, g, b)
        self.setx(600)
        self.sety(random.randint(-250, 250))
        self.setheading(180)

    def move(self, level):
        self.forward(3 * level)
