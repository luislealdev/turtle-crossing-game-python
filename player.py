from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("Black")
        self.start_from_bottom()
        self.setheading(90)
    
    def move(self):
        self.forward(MOVE_DISTANCE)

    def start_from_bottom(self):
        self.goto(STARTING_POSITION)
    
    

