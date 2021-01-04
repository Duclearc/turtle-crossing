import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Game setup
player = Player(screen.window_height())
cars = CarManager(screen.window_height(), screen.window_width())
score = Scoreboard(screen.window_height(), screen.window_width())
game_is_on = True

# Gameplay setup
screen.listen()
screen.onkeypress(player.go_up, 'Up')
screen.onkeypress(player.go_down, 'Down')


def detect_collision():
    """detects if the player has come into contact with any of the cars and triggers the game_over sequence if so"""
    global game_is_on
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()


def detect_victory():
    """detects if the player is at the finish line. If so, resets it's position and increases the score."""
    if player.reached_finish_line():
        score.level_up()
        cars.increase_cars_speed()


while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    detect_collision()
    detect_victory()

screen.exitonclick()
