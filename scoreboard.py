from turtle import Turtle
alignment = 'center'
font = ("Arial", 24,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=alignment, font=font)
        self.goto(100, 200)
        self.write(self.r_score, align=alignment, font=font)


    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

#     def game_over(self):
#         self.goto(0, 0)
#         self.color("white")
#         self.write(f"Game over!", align=alignment, font=font)
