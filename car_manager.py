import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(name="square")   
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(310,random.randint(-250, 250))

    def move(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x,self.ycor())