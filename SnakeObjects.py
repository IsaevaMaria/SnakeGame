from random import choice

SCREEN_SIZE = 500, 400
SIZE_RECT = 20
class Cell:
    def __init__(self, x, y):
        self.coord = x, y
        self.move = [-1, 0]

    def get_coord(self):
        return self.coord

    def set_coord(self, x, y):
        self.coord = x, y

    def get_move(self):
        return self.move

    def set_move(self, x, y):
        if x in range(-1, 2) and y in range(-1, 2):
            self.move[0] = x
            self.move[1] = y

class Snake:
    def __init__(self, x, y):
        self.snake = [Cell(x, y), Cell(x + SIZE_RECT, y), Cell(x + 2 * SIZE_RECT, y)]

    def get_head_coords(self):
        return self.snake[0].get_coord()

    def set_head_coords(self, s):
        self.snake[0].set_coord(s[0], s[1])

    def get_head(self):
        return self.snake[0]

    def get_snake(self):
        return [x.get_coord() for x in self.snake]

    def change_move(self, x, y):
        for i in range(len(self.snake) - 2, -1, -1):
            s, d = self.snake[i].get_move()
            self.snake[i + 1].set_move(s, d)
        self.snake[0].set_move(x,y)
        for f in self.snake:
            x = (f.get_coord()[0] + SIZE_RECT * f.get_move()[0]) % SCREEN_SIZE[0]
            y = (f.get_coord()[1] + SIZE_RECT * f.get_move()[1]) % SCREEN_SIZE[1]
            f.set_coord(x, y)

    def change_len(self):
        x, y = self.snake[-1].get_coord()
        s, d = self.snake[-1].get_move()
        x1 = x - SIZE_RECT * s
        y1 = y - SIZE_RECT * d
        new_object = Cell(x1, y1)
        new_object.set_move(s, d)
        self.snake.append(new_object)

class Food:
    def __init__(self):
        self.food = []
        self.level = 1
        self.count_food = 1
        self.generate_food()

    def generate_food(self):
        self.food = [(choice(range(SIZE_RECT, SCREEN_SIZE[0] - SIZE_RECT , SIZE_RECT)), \
                      choice(range(SIZE_RECT, SCREEN_SIZE[1] - SIZE_RECT , SIZE_RECT))) \
                     for i in range(self.count_food)]

    def get_food(self):
        return self.food

    def set_food(self, list_food):
        self.food = list_food[:]




