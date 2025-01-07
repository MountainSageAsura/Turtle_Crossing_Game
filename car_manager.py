from turtle import Turtle, colormode
import random
import time

# change color mode to use rgb
colormode(255)

# color list to be used for selection
COLORS = [(240, 207, 239), (126, 148, 205), (246, 197, 102), (254, 111, 96), (242, 233, 159), (152, 215, 170), (41, 45, 78), (48, 48, 80), (122, 97, 92), (254, 94, 80), (75, 73, 113)]

# car shape size parameters
WIDTH_MULT = 1
LENGTH_MULT = 2


# car move distance
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# car generation coordinates
CAR_LOW_LIMIT = -250
CAR_HIGH_LIMIT = 250


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=WIDTH_MULT, stretch_len=LENGTH_MULT)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(CAR_LOW_LIMIT, CAR_HIGH_LIMIT)
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
