from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "w")


car_list = []
game_on = True
counter = 0
for i in range(15):
    car = Car()
    car.setx(random.randint(0, 400))
    car_list.append(car)

while game_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    scoreboard.update_scoreboard()

    if counter % 4 == 0:
        new_car = Car()
        car_list.append(new_car)
    for car in car_list:
        car.move(scoreboard.level)
    for car in car_list:
        if car.distance(player) < 22:
            scoreboard.game_over()
            game_on = False
    if player.ycor() > 280:
        player.setpos(0, -270)
        scoreboard.level += 1





screen.exitonclick()