from turtle import Turtle

FONT_SIZE = 24
FONT = ("Courier", FONT_SIZE, "normal")
BUFFER = FONT_SIZE + 10


class Scoreboard(Turtle):
    def __init__(self, screen_height, screen_width):
        super().__init__()
        self.SCREEN_HEIGHT = int(screen_height / 2) - BUFFER
        self.SCREEN_WIDTH = int(screen_width / 2) - BUFFER
        self.level = 0
        self.ht()
        self.penup()
        self.speed('fastest')
        self.goto(x=-self.SCREEN_WIDTH, y=self.SCREEN_HEIGHT)
        self.update_score()

    def level_up(self):
        """increases the level by 1 and updates the score"""
        self.level += 1
        self.update_score()

    def update_score(self):
        """clears the old level text and rewrites it with the updated level"""
        self.clear()
        self.write(arg=f'Level: {self.level}', align='left', font=FONT)

    def game_over(self):
        """writes 'GAME OVER' at the center of the screen"""
        self.home()
        self.write(arg='GAME OVER', align='center', font=FONT)
