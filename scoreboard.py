from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 270)
        self.write(f"Level: {self.level}", align="center", font=("Arial", 18, "normal"))

    def point(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
