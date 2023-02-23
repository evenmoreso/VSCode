from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "Center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level_num = 1
        self.color("black")
        self.speed("fastest")
        self.goto(-230,270)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Level: {self.level_num}", move=False, align = ALIGNMENT, font=FONT)

    def next_level(self):
        self.level_num += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def highest_level(self):
        self.goto(0, -30)
        self.write(f"YOUR HIGHEST SCORE IS: {self.level_num}", move=False, align=ALIGNMENT, font=FONT)
