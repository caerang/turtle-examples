import turtle


class WorldBorder:
    limit_x: float
    limit_y: float

    def __init__(self, size_x, size_y) -> None:
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.limit_x = size_x / 2 - 15
        self.limit_y = size_y / 2 - 15

        border = turtle.Turtle()
        border.speed(0)
        border.color("white")
        border.penup()
        border.setpos(-400, -350)
        border.pendown()
        border.pensize(4)

        for i in range(4):
            if i % 2 == 0:
                border.fd(size_x)
            else:
                border.fd(size_y)
            border.lt(90)
        border.hideturtle()


class World:
    world_border: WorldBorder

    def __init__(self) -> None:
        super().__init__()
        self.world_border = WorldBorder(800, 700)
    
    def get_border_x(self):
        return self.world_border.size_x / 2
