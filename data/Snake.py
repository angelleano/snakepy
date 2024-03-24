# Snake class

from data.Block import Block


class Snake():
    def __init__(self, field):
        self.width = field.width
        self.height = field.height
        self.direction = "Right"
        self.body = [field.blocks[1], field.blocks[2]]
        self.tail = self.body[0]
        self.head = self.body[-1]

    def draw(self):
        for block in self.body:
            block.snake = True

    def opposite(self):
        match self.direction:
            case "Up":
                return "Down"
            case "Down":
                return "Up"
            case "Left":
                return "Right"
            case "Right":
                return "Left"

    def move_forward(self, field):
        last_x = self.head.x
        last_y = self.head.y
        match self.direction:
            case "Up":
                new_block = field.get_block_by_pos(last_x, last_y - 25)
            case "Down":
                new_block = field.get_block_by_pos(last_x, last_y + 25)
            case "Left":
                new_block = field.get_block_by_pos(last_x - 1, last_y)
            case "Right":
                new_block = field.get_block_by_pos(last_x + 1, last_y)
        self.body.append(new_block)
        self.body[0].snake = False
        self.body.pop(0)
        self.tail = self.body[0]
        self.head = self.body[-1]
