from turtle import Turtle

MOVE_DISTANCE = 10
TURTLE_HEIGHT = 20


class Player(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.FINISH_LINE_Y = int(screen_height/2) - TURTLE_HEIGHT
        self.STARTING_POSITION = (0, -self.FINISH_LINE_Y)
        self.shape('turtle')
        self.penup()
        self.speed('fastest')
        self.reset_position()
        self.setheading(90)

    def go_up(self):
        """moves the player up by a predetermined amount"""
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        """moves the player down by a predetermined amount"""
        if self.ycor() > -self.FINISH_LINE_Y:
            self.backward(MOVE_DISTANCE)

    def reset_position(self):
        """resets the player's position at the bottom of the screen"""
        self.goto(self.STARTING_POSITION)

    def reached_finish_line(self):
        """returns True and returns player to STARTING_POSITION if player is at finish line. Else returns False"""
        if self.ycor() > self.FINISH_LINE_Y:
            self.reset_position()
            return True
        else:
            return False
