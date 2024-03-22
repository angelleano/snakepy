# Block class

import pygame

class Block():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.abs_x = x * self.width
        self.abs_y = y * self.height
        self.color = (100, 100, 100)
        self.snake_color = (75, 245,66) 
        self.snake = False
        self.rect = pygame.Rect(self.abs_x, self.abs_y, self.width, self.height)

    def draw(self, display):
        if self.snake:
            pygame.draw.rect(display, self.snake_color, self.rect)
        else:
            pygame.draw.rect(display, self.color, self.rect)