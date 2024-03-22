# Field class

import pygame
from data.Block import Block

class Field():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.block_width = width // 25
        self.block_height = height // 25
        self.blocks = self.gen_blocks()

    def gen_blocks(self):
        blocks = []
        for y in range(25):
            for x in range(25):
                blocks.append(Block(x, y, self.block_width, self.block_height))
        return blocks

    def draw(self, display):
        for block in self.blocks:
            block.draw(display)