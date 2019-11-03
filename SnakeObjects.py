from random import choice


class Cell:
    def __init__(self, x, y):
        self.coord = x, y
        self.move = [-1, 0]

    def get_coord(self):
        return self.coord

    def set_coord(self, x, y):
        print(x, y)
        self.coord = x, y

    def get_move(self):
        return self.move

    def set_move(self, x, y):
        try:
            if x in range(-1, 2) and y in range(-1, 2):
                self.move[0] = x
                self.move[1] = y
                print(x, y)

        except:
            pass


class Snake:
    def __init__(self, x, y):
        self.snake = [Cell(x, y), Cell(x + 20, y), Cell(x + 40, y)]

    def get_head_coords(self):
        return self.snake[0].get_coord()

    def get_head(self):
        return self.snake[0]

    def get_snake(self):
        return [x.get_coord() for x in self.snake]

    def terra(self, x, y):
        for i in range(len(self.snake) - 2, -1, -1):
            s, d = self.snake[i].get_move()
            self.snake[i + 1].set_move(s, d)
        self.snake[0].set_move(x,y)
        for f in self.snake:
            f.set_coord(f.get_coord()[0] + 20 * f.get_move()[0], f.get_coord()[1] + 20 * f.get_move()[1] )





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

