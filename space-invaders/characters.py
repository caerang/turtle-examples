import math
import turtle


class Entity:
    speed: int
    alive: bool
    body: turtle.Turtle

    limit_x: float
    limit_y: float

    def __init__(self, x, y, speed, color, sprite, limit_x, limit_y) -> None:
        super().__init__()
        self.alive = True
        self.body = turtle.Turtle()
        self.speed = speed
        self.limit_x = limit_x
        self.limit_y = limit_y

        # Create the body
        self.body.hideturtle()
        self.body.color(color)
        self.body.shape(sprite)
        self.body.penup()
        self.body.speed(0)
        self.body.setposition(x, y)
        self.body.setheading(90)
        self.body.showturtle()

    def move(self):
        self.body.forward(self.speed)

    def collision(self, other):
        try:
            dist_x = math.pow(self.body.xcor() - other.body.xcor(), 2)
            dist_y = math.pow(self.body.ycor() - other.body.ycor(), 2)
            distance = math.sqrt(dist_x + dist_y)

            if distance < 20:
                self.body.hideturtle()
                del self

                other.body.hideturtle()
                del other
        except:
            raise TypeError("Isn't a collider")


class Bullet(Entity):
    def __init__(self, x, y, limit_x, limit_y) -> None:
        super().__init__(x=x, y=y, speed=20, color="yellow", sprite="triangle", limit_x=limit_x, limit_y=limit_y)
        self.body.shapesize(0.5, 0.5)

    def move(self):
        y = self.body.ycor() + self.speed
        if self.body.ycor() < self.limit_y:
            self.body.sety(y)
        else:
            self.body.hideturtle()
            del self


class Enemy(Entity):
    def __init__(self, x, y, speed, color, sprite, limit_x, limit_y) -> None:
        super().__init__(x, y, speed, color, sprite, limit_x, limit_y)

    def move(self):
        x = self.body.xcor() + self.speed
        if x < self.limit_x and x > -self.limit_x:
            self.body.setx(x)
        else:
            self.body.sety(self.body.ycor()-30)
            self.speed = -self.speed


class Player(Entity):
    lifes: int
    score: int
    fire: float
    fire_rate: float
    bullets = list

    def __init__(self, x, y, speed, color, sprite, limit_x, limit_y) -> None:
        super().__init__(x, y, speed, color, sprite, limit_x, limit_y)
        self.lifes = 3
        self.score = 0
        self.fire = 0
        self.fire_rate = 5
        self.bullets = []

    def move_left(self):
        x = self.body.xcor() - (2 * self.speed)
        if x > -self.limit_x:
            self.body.setx(x)

    def move_right(self):
        x = self.body.xcor() + (2 * self.speed)
        if x < self.limit_x:
            self.body.setx(x)

    def shoot(self):
        if self.fire > self.fire_rate:
            self.fire = 0
            self.bullets.append(Bullet(self.body.xcor(), self.body.ycor()+15, self.limit_x, self.limit_y))


class EnemyWave:
    Wave: int = 1
    WaveDifficult: int = 1
    enemies: list

    def __init__(self, quantity, limit_x, limit_y) -> None:
        super().__init__()
        self.enemies = []

        x = limit_x - 30
        y = limit_y - 30
        for i in range(quantity):
            self.enemies.append(Enemy(
                x = -x, y = y, speed = EnemyWave.WaveDifficult,
                color="red", sprite="circle",
                limit_x = limit_x, limit_y = limit_y
            ))

            x -= 30
            if x >= limit_x:
                x = limit_x
                y -= 30
