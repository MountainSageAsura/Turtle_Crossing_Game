from turtle import Screen
import  time
from player import Player

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("My Turtle Crossing Game")
screen.tracer(0)


player = Player()
screen.listen()
screen.onkey(player.move, key="w")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)




screen.exitonclick()