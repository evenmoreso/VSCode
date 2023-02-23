from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# Expanation of why we dont use the super parent class:
    #The other classes we created were a single object of the Turtle class. The class we created was in fact a single Turtle Object.. 
    #But the CarManager wasn't just one single object, we created a list of Turtle Objects. If the CarManager was a single object but was duplicated many times around the screen, when we'd change the color it would change the color of every single duplication across the screen.
    #But instead we created a list inside the CarManager of turtle objects so we could style, and control each completely by itself.

# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.parking_lot = []

#     def create_car(self):
#         self.penup()
#         self.shape("square")
#         self.shapesize(stretch_wid=1, stretch_len=2)
#         self.color(random.choice(COLORS))
#         self.goto(300, random.randint(-280,280))
#         self.parking_lot.append(self)
        
#     def move(self):
#         for car in self.parking_lot:
#             self.backward(STARTING_MOVE_DISTANCE)


class CarManager:
    def __init__(self):
        self.parking_lot = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6) # SO MART! Use this method to slow down the speed of creating new object
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-280,280))
            self.parking_lot.append(new_car)
        
    def move(self):
        for car in self.parking_lot:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
        self.move()
        



