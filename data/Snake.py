# Snake class

from data.Block import Block


class Snake():
    def __init__(self, field):
        width = field.width
        height = field.height
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

    def move_forward(self):
        last_x = self.head.x
        last_y = self.head.y
        match self.direction:
            case "Up":
                new_block = Block(last_x, last_y - 1, width, height)
            case "Down":
                new_block = Block(last_x, last_y + 1, width, height)
            case "Left":
                new_block = Block(last_x - 1, last_y, width, height)
            case "Right":
                new_block = Block(last_x + 1, last_y, width, height)
        self.body.append(new_block)
        self.body.pop(0)

