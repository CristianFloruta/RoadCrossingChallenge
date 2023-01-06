import time
from turtle import Screen
from player import Player
from carManager import CarManager
from scoreBoard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Road Crossing Challenge")
screen.tracer(0)

player = Player()
car = CarManager()

# movement control
screen.listen()
screen.onkeypress(key="space", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_forward()
    # detect player road crossing successfully
    if player.ycor() > 280:
        player.goto_start()

screen.exitonclick()
