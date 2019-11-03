import pygame
from SnakeObjects import Cell, Snake, Food, Game

pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)


class Game:
    def __init__(self):
        self.sn = Snake(100, 100)
        self.fd = Food()
        self.cell_size = 20

    def render(self):
        for f in self.sn.get_snake():
            pygame.draw.rect(screen, pygame.Color("white"), (f[0], f[1], self.cell_size, self.cell_size))

    def draw_food(self):
        for f in self.fd.get_food():
            pygame.draw.rect(screen, pygame.Color("red"), (f[0], f[1], self.cell_size, self.cell_size))

game = Game()
running = True
x, y = game.sn.get_head_coords()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += 10
    screen.fill((0, 0, 0))
    game.render()
    game.draw_food()
    pygame.display.flip()
pygame.quit()
