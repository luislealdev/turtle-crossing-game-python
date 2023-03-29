import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

screen.onkey(player.move, "Up")

car_list = []
game_is_on = True

counter = 0
while game_is_on:
    time.sleep(0.1)
    if counter == 6:
        new_car = CarManager()
        car_list.append(new_car)
        counter=0
    for car in car_list:
        car.move()
    screen.update()

    for car in car_list:
        if abs(car.xcor() - player.xcor()) < 21 or abs(car.ycor() - player.ycor()) < 11:
            game_is_on = False
    counter+=1

