# Snake class

from data.Block import Block


class Snake():
    def __init__(self, field):
        self.width = field.width
        self.height = field.height
        self.direction = "right"
        self.body = [field.blocks[1], field.blocks[2]]
        self.tail = self.body[0]
        self.head = self.body[-1]

    def draw(self):
        for block in self.body:
            block.snake = True

    def opposite(self):
        match self.direction:
            case "up":
                return "down"
            case "down":
                return "up"
            case "left":
                return "right"
            case "right":
                return "left"

    def move_forward(self, field):
        last_x = self.head.x
        last_y = self.head.y
        match self.direction:
            case "up":
                new_block = field.get_block_by_pos(last_x, last_y - 1)
            case "down":
                new_block = field.get_block_by_pos(last_x, last_y + 1)
            case "left":
                new_block = field.get_block_by_pos(last_x - 1, last_y)
            case "right":
                new_block = field.get_block_by_pos(last_x + 1, last_y)
        self.body.append(new_block)
        self.body[0].snake = False
        self.body.pop(0)
        self.tail = self.body[0]
        self.head = self.body[-1]
