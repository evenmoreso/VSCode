import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
cars = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(tim.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    # Detects collision with cars: 1) stop the game; 2) show "Game over"
    for car in cars.parking_lot:
        if tim.distance(car) < 15:
            game_is_on =  False
            scoreboard.game_over()
            scoreboard.highest_level()

    # Detects collision with top wall: 1) Score + 1; 2) Turtle goes back to starting point; 3) Cars spead up
    if tim.ycor()>280:
        scoreboard.next_level()
        tim.reset_position()
        cars.speed_up()

screen.exitonclick()
