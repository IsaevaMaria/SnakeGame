import random


class Cell:
    def __init__(self, x, y):
        self.coord = x, y

    def get_coord(self):
        return self.coord


class Snake:
    def __init__(self):
        self.shake = [Cell(5, 5)]

    def get_head_coords(self):
        return self.snake[0].coord

    def get_snake(self):
        return [x.get_coord() for x in self.snake]


class Food:
    def __init__(self):
        self.food = []
        self.level = 1
        self.count_food = 1

    def generate_food(self):
        self.food = [(random.randint(30), random.randint(30)) for _ in self.count_food]


class Game:
    def __init__(self):
        self.sn = Snake()
        self.fd = Food()
