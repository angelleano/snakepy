import pygame
from data.Field import Field
from data.Block import Block
from data.Snake import Snake

pygame.init()

WINDOW_SIZE = (800, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)

field = Field(WINDOW_SIZE[0], WINDOW_SIZE[1])
snake = Snake(field)

def draw(display):
    display.fill("white")
    snake.draw()
    field.draw(display)
    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not field.has_food:
        field.gen_food()
    snake.move_forward(field)
    draw(screen)
    pygame.time.delay(500)