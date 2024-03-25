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
    if not field.has_food:
        field.gen_food()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            direction = pygame.key.name(event.key)
            if direction == "up" and direction != snake.opposite():
                snake.direction = "up"
                break
            if direction == "down" and direction != snake.opposite():
                snake.direction = "down"
                break
            if direction == "left" and direction != snake.opposite():
                snake.direction = "left"
                break
            if direction == "right" and direction != snake.opposite():
                snake.direction = "right"
                break
    
    if snake.head == field.food:
        snake.grow(field)
        field.food.food = False
        field.gen_food()
    else:
        if not snake.move_forward(field):
            print("Game Over")
            running = False
    
    draw(screen)
    pygame.time.delay(150)