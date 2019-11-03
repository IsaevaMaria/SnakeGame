import pygame
from SnakeObjects import Cell, Snake, Food, Game

pygame.init()
size = 350, 450
screen = pygame.display.set_mode(size)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, x, y):
        pygame.draw.rect(screen, pygame.Color("white"), (x, y, 10, 10))



    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, cell):
        for i in range(self.width):
            self.board[cell[1]][i] = (self.board[cell[1]][i] + 1) % 2
        for i in range(self.height):
            if i == cell[1]:
                continue
            self.board[i][cell[0]] = (self.board[i][cell[0]] + 1) % 2

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


board = Board(5, 7)
board.set_view(50, 50, 50)

running = True
g = Game()
x, y = 100, 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += 10
    screen.fill((0, 0, 0))
    board.render(x, y)
    pygame.display.flip()
pygame.quit()
