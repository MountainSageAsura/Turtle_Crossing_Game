from turtle import Turtle

X_POSITION = 0
Y_POSITION = -280
MOVE_FORWARD_DISTANCE = 20
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.shape("turtle")
        self.color("DarkSeaGreen3")
        self.penup()
        self.setheading(90)
        self.goto(x=X_POSITION, y=Y_POSITION)

    def move(self):
        self.forward(MOVE_FORWARD_DISTANCE)
        # Detect collision with the wall
        if self.ycor() >= FINISH_LINE_Y:
            self.reset_turtle()

    def reset_turtle(self):
        self.goto(x=X_POSITION, y=Y_POSITION)