# Field class

import pygame
import random
from data.Block import Block

class Field():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.block_width = width // 25
        self.block_height = height // 25
        self.blocks = self.gen_blocks()
        self.has_food = False
        self.food = None

    def gen_blocks(self):
        blocks = []
        for y in range(25):
            for x in range(25):
                blocks.append(Block(x, y, self.block_width, self.block_height))
        return blocks

    def get_block_by_pos(self, x, y):
        n = x + (y*25)
        return self.blocks[n]

    def gen_food(self):
        new_pos = random.randrange(0, 625)
        self.blocks[new_pos].food = True
        self.has_food = True
        self.food = self.blocks[new_pos]
        return self.blocks[new_pos]

    def draw(self, display):
        for block in self.blocks:
            block.draw(display)