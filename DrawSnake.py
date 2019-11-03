import pygame
from SnakeObjects import Cell, Snake, Food

pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Игра "Змейка"')

class Game:
    def __init__(self):
        self.sn = Snake(100, 100)
        self.fd = Food()
        self.cell_size = 20

    def change_snake(self):
        self.fd.generate_food()
        self.sn.change_len()

    def convertion(self, x, y):
        if self.sn.get_head().get_move()[0] * x != -1 and self.sn.get_head().get_move()[1] * y != -1:
            self.sn.change_move(x, y)

    def render(self):
        i = 0
        for f in self.sn.get_snake():
            if i == 0:
                pygame.draw.rect(screen, pygame.Color("blue"), (f[0], f[1], self.cell_size, self.cell_size))
            else:
                pygame.draw.rect(screen, pygame.Color("white"), (f[0], f[1], self.cell_size, self.cell_size))
            i += 1

    def draw_food(self):
        for f in self.fd.get_food():
            pygame.draw.rect(screen, pygame.Color("red"), (f[0], f[1], self.cell_size, self.cell_size))

    def eat_food(self):
        s_coord = self.sn.get_head_coords()
        self.fd.set_food([f for f in self.fd.get_food() if not(f[0] == s_coord[0] and f[1] == s_coord[1])])

    def is_food_empty(self):
        if len(self.fd.get_food()) != 0:
            return True
        s_coord = self.sn.get_head_coords()
        return False


game = Game()
running = True
x, y = game.sn.get_head_coords()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            game.convertion(-1, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            game.convertion(1, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            game.convertion(0, -1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            game.convertion(0, 1)

    screen.fill((0, 0, 0))
    game.render()
    game.eat_food()
    if not game.is_food_empty():
        game.change_snake()
    game.draw_food()
    pygame.display.flip()
pygame.quit()
