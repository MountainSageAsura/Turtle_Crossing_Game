from turtle import Screen
import  time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("My Turtle Crossing Game")
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, key="Up")

index = 0
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()


    car_manager.create_car()
    car_manager.move_car()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()

    # Detect collision between turtle and car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            is_game_on = False


screen.exitonclick()