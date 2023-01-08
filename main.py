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
car_manager = CarManager()
score = Scoreboard()

# movement control
screen.listen()
screen.onkeypress(key="space", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # create and move cars
    car_manager.create_car()
    car_manager.move_car()
    # detect player road crossing successfully
    if player.ycor() > 280:
        player.goto_start()
        car_manager.increase_speed()
        score.level_up()
    # detect player car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            score.game_over()
            game_is_on = False

screen.exitonclick()
