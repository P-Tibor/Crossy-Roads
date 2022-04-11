from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape("turtle")
        self.setpos(0, -270)
        self.color("black")
        self.setheading(90)

    def move(self):
        self.forward(10)
