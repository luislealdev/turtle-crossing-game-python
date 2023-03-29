from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.level+=1
        self.clear()
        self.goto(-250,250)
        self.write(f"Level: {self.level}" , align="left", font=FONT)

    def show_game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

