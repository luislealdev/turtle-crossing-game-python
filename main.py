import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

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
        if car.xcor()<20 and car.xcor()>-20 and abs(car.ycor() - player.ycor()) < 10:
            game_is_on = False
    
    if player.ycor() > FINISH_LINE_Y:
        player.start_from_bottom()
        for car in car_list:
            car.increase_velocity()
    counter+=1

