from random import choice


class Cell:
    def __init__(self, x, y):
        self.coord = x, y

    def get_coord(self):
        return self.coord


class Snake:
    def __init__(self, x, y):
        self.snake = [Cell(x, y)]

    def get_head_coords(self):
        return self.snake[0].get_coord()

    def get_snake(self):
        return [x.get_coord() for x in self.snake]


class Food:
    def __init__(self):
        self.food = []
        self.level = 1
        self.count_food = 1
        self.generate_food()

    def generate_food(self):
        self.food = [(choice(range(20, 400, 20)), choice(range(20, 400, 20))) for i in range(self.count_food)]

    def get_food(self):
        return self.food


class Game:
    def __init__(self):
        self.sn = Snake()
        self.fd = Food()

